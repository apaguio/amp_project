import requests
import time
from app import celery
from celery.utils.log import get_task_logger
import xml.etree.ElementTree as ET
from datetime import datetime
from redis import Redis
from models import db, influxdb
from models.utils import get_tariff_details
from lib import emailer, sms
from pymodbus.client.sync import ModbusTcpClient
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.constants import Endian

logger = get_task_logger(__name__)
redis = Redis()

@celery.task(name='tasks.accuenergy.collect')
def accuenergy_collect():
    client = ModbusTcpClient('108.174.20.70', 4502)
    def _decode_result(result):
        decoder = BinaryPayloadDecoder.fromRegisters(result.registers, endian=Endian.Big)
        return decoder.decode_32bit_float()
    # read voltage value
    result = client.read_holding_registers(0x4002, 2, unit=1)
    V = round(_decode_result(result), 2)

    # read power value
    result = client.read_holding_registers(0x401c, 2, unit=1)
    P = round(_decode_result(result), 2)

    # read power factor value
    result = client.read_holding_registers(0x4034, 2, unit=1)
    PF = round(_decode_result(result), 2)

    utc_now = datetime.utcfromtimestamp(time.time())
    utc_timestamp = int((utc_now - datetime(1970, 1, 1)).total_seconds())

    data = {'name': 'accuenergy_test',
            'columns': ['time', 'P', 'L1_PF', 'L1_V'],
            'points': [[utc_timestamp, P, PF, V],]}
    influxdb.write_points([data])
    return data

@celery.task(name="tasks.ekm.collect")
def ekm_collect(meter_id, nr_readings, key, endpoint='io.ekmpush.com', simulate_solar=False):
    def _compute_pf(pf):
        if pf < 100:
            pf = pf / 100.0
        elif pf > 100:
            pf = (200 - pf) / 100.0
        else:
            pf = 1
        return pf
    uri = 'http://%s/%s~%s.xml?%s' % (endpoint, meter_id, nr_readings, key)
    ekm_data = requests.get(uri).content
    data = {'name': meter_id, 'columns': ['time', 'P', 'L1_PF', 'L1_V'], 'points': []}
    if not simulate_solar:
        data['name'] = '10054'
    root = ET.fromstring(ekm_data)
    for read in root.iter('read'):
        #seq = (long(read.get('seq'))/1000) - 300 # -300 seconds, fix ekm bug +5 mins
        seq = (long(read.get('seq'))/1000) # apparently they fixed the +5mins issue
        utc_reading = datetime.utcfromtimestamp(seq)
        utc_seq = int((utc_reading - datetime(1970, 1, 1)).total_seconds()) # save points in db with UTC timestamps
        P = long(read.get('P')) # TODO: measured by W, to be converted to kW (i.e: /1000)
        if simulate_solar:
            P = P / 3
        L1_PF = _compute_pf(int(read.get('L1_PF')))
        L1_V = int(read.get('L1_V')) / 10
        point = [utc_seq, P, L1_PF, L1_V]
        data['points'].append(point)

    # Publishing to pubsub when event occurs, to be sent by socket.io
    publish_msg = {'meter_id': meter_id, 'points': data['points']}
    redis.publish('point', publish_msg)

    # Write to influxdb
    influxdb.write_points([data])

@celery.task(name='tasks.ekm.meter.resolution.aggregator')
def ekm_meter_aggregate_with_resolution(meter_id, resolution):
    utc_now = datetime.utcfromtimestamp(time.time())
    query = 'select mean(P), mean(L1_PF), mean(L1_V) from "%s" where time > now() - %s;' % (meter_id, resolution)
    query_result = influxdb.query(query)
    if query_result:
        result_point = query_result[0]['points'][0]
        utc_timestamp = int((utc_now - datetime(1970, 1, 1)).total_seconds())
        data = {'name': '%s_%s' % (meter_id, resolution), 'columns': ['time', 'P', 'L1_PF', 'L1_V'],
                'points': [[utc_timestamp, result_point[1], result_point[2], result_point[3]]]}
        influxdb.write_points([data])

@celery.task(name='tasks.ekm.facility.15mins.aggregator')
def ekm_facility_aggregate(user_name, meter_id, solar_meter_id):
    utc_now = datetime.utcfromtimestamp(time.time())
    tariff_data = get_tariff_details(user_name)

    facility_query = 'select mean(P) as demand from "%s" where time > now() - 15m;' % meter_id
    facility_result = influxdb.query(facility_query)
    demand = round(facility_result[0]['points'][0][1], 2)

    solar_power = 0
    solar_query = 'select mean(P) as demand from "%s" where time > now() - 15m;' % solar_meter_id
    solar_result = influxdb.query(solar_query)
    if solar_result:
        solar_power = round(solar_result[0]['points'][0][1], 2)
    net_load = demand - solar_power

    utc_timestamp = int((utc_now - datetime(1970, 1, 1)).total_seconds())
    data = {'name': '%s_15mins_%s_%s' % (meter_id, tariff_data['season'], tariff_data['peak_period']), 'columns': ['time', 'demand'],
            'points': [[utc_timestamp, net_load]]}
    influxdb.write_points([data])

@celery.task(name='tasks.energy.1h.aggregator')
def energy_1h_aggregate(user_name, meter_id):
    utc_now = datetime.utcfromtimestamp(time.time())
    tariff_data = get_tariff_details(user_name)

    energy_query = 'select mean(P) from "%s" where time > now() - 1h;' % meter_id
    energy_query_result = influxdb.query(energy_query)
    energy = round(energy_query_result[0]['points'][0][1], 2)

    utc_timestamp = int((utc_now - datetime(1970, 1, 1)).total_seconds())
    data = {'name': '%s_energy_1h_%s_%s' % (meter_id, tariff_data['season'], tariff_data['peak_period']), 'columns': ['time', 'energy_kwh'],
            'points': [[utc_timestamp, energy]]}
    influxdb.write_points([data])

def _send_alerts(current_user, title, msg):
    if current_user.alerts_emails:
        emailer.send_email(current_user.alerts_emails, title, msg)
    if current_user.alerts_phones:
        for phone in current_user.alerts_phones:
            sms.send(phone, msg)
    current_user.last_alerted = int(time.time())
    current_user.save()

def _can_send_alert(current_user):
    time_diff = datetime.fromtimestamp(time.time()) - datetime.fromtimestamp(current_user.last_alerted)
    return time_diff.total_seconds() > (current_user.alert_frequency_in_minutes * 60)

@celery.task(name='tasks.one.minute.netload.avg.check')
def netload_avg_check(user_name, meter_id, solar_meter_id):
    current_user = db.Customer.objects(name=user_name).first()
    if _can_send_alert(current_user):
        if current_user.one_minute_netload_avg_threshold and (current_user.alerts_emails or current_user.alerts_phones):
            facility_query = 'select mean(P) from "%s" where time > now() - 1m;' % meter_id
            facility_result = influxdb.query(facility_query)
            demand = round(facility_result[0]['points'][0][1], 2)

            solar_power = 0
            solar_query = 'select mean(P) from "%s" where time > now() - 1m;' % solar_meter_id
            solar_result = influxdb.query(solar_query)
            if solar_result:
                solar_power = round(solar_result[0]['points'][0][1], 2)
            net_load = demand - solar_power

            if net_load > current_user.one_minute_netload_avg_threshold:
                title = 'WARNING: Net load average exceeded threshold'
                msg = 'Net load average (currently %s kW) just exceeded your current threshold %s kW' % (net_load, current_user.one_minute_netload_avg_threshold)
                _send_alerts(current_user, title, msg)

@celery.task(name='tasks.power.factor.check')
def power_factor_check(user_name, meter_id):
    current_user = db.Customer.objects(name=user_name).first()
    if _can_send_alert(current_user):
        if current_user.power_factor_threshold and (current_user.alerts_emails or current_user.alerts_phones):
            power_factor_query = 'select mean(L1_PF) from "%s" where time > now() - 30s;' % meter_id
            power_factor_query_result = influxdb.query(power_factor_query)
            power_factor = round(power_factor_query_result[0]['points'][0][1], 2)

            if power_factor < current_user.power_factor_threshold:
                msg = 'Power factor (currently %s) just went below your current threshold %s' % (power_factor, current_user.power_factor_threshold)
                title = 'WARNING: Power factor went below threshold'
                _send_alerts(current_user, title, msg)

@celery.task(name='tasks.voltage.check')
def voltage_check(user_name, meter_id):
    current_user = db.Customer.objects(name=user_name).first()
    if _can_send_alert(current_user):
        if current_user.voltage_threshold and (current_user.alerts_emails or current_user.alerts_phones):
            voltage_query = 'select mean(L1_V) from "%s" where time > now() - 30s;' % meter_id
            voltage_query_result = influxdb.query(voltage_query)
            voltage = round(voltage_query_result[0]['points'][0][1], 2)

            if (voltage < 120 - current_user.voltage_threshold):
                msg = 'Voltage (currently %s) just went below your current threshold %s' % (voltage, 120 - current_user.voltage_threshold)
                title = 'WARNING: Voltage went below threshold'
                _send_alerts(current_user, title, msg)
            elif (voltage > 120 + current_user.voltage_threshold):
                msg = 'Voltage (currently %s) just went above your current threshold %s' % (voltage, 120 + current_user.voltage_threshold)
                title = 'WARNING: Voltage went above threshold'
                _send_alerts(current_user, title, msg)
