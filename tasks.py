import requests
import time
from app import celery
from celery.utils.log import get_task_logger
import xml.etree.ElementTree as ET
from datetime import datetime
from models import db, influxdb
from models.utils import get_tariff_details

logger = get_task_logger(__name__)

@celery.task(name="tasks.ekm.collect")
def ekm_collect(user_id, meter_id, nr_readings, key, endpoint='io.ekmpush.com', simulate_solar=False):
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
    data = {'name': '%s_%s' % (user_id, meter_id), 'columns': ['time', 'P', 'L1_PF', 'L1_V'], 'points': []}
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
    influxdb.write_points([data])

@celery.task(name='tasks.ekm.facility.15mins.aggregator')
def ekm_facility_aggregate(user_id, meter_id):
    utc_now = datetime.utcfromtimestamp(time.time())
    tariff_data = get_tariff_details(user_id)

    facility_query = 'select mean(P) as demand from "%s_%s" where time > now() - 15m;' % (user_id, meter_id)
    facility_result = influxdb.query(facility_query)
    demand = round(facility_result[0]['points'][0][1], 2)

    utc_timestamp = int((utc_now - datetime(1970, 1, 1)).total_seconds())
    data = {'name': '%s_%s_15mins_%s_%s' % (user_id, meter_id, tariff_data['season'], tariff_data['peak_period']), 'columns': ['time', 'demand'],
            'points': [[utc_timestamp, demand]]}
    influxdb.write_points([data])

@celery.task(name='tasks.netload.aggregator')
def ekm_netload_aggregate(user_id, interval):
    user = db.Customer.objects(id=user_id).first()
    utc_now = datetime.utcfromtimestamp(time.time())
    tariff_data = get_tariff_details(user_id)
    consumption = 0.0
    generation = 0.0
    query = 'select mean(P) from /^%s_\d+$/ where time > now() - %s;' % (user_id, interval)
    query_result = influxdb.query(query)
    facility_meters_ids = [meter.id for meter in user.facility]
    solar_meters_ids = [meter.id for meter in user.solar]
    for result in query_result:
        meter_id = result['name'].split('_')[1]
        if meter_id in facility_meters_ids:
            consumption += round(result['points'][0][1], 2)
        elif meter_id in solar_meters_ids:
            generation += round(result['points'][0][1], 2)

    netload = consumption - generation
    utc_timestamp = int((utc_now - datetime(1970, 1, 1)).total_seconds())
    data = {'name': '%s_%s_%s_%s' % (user_id, interval, tariff_data['season'], tariff_data['peak_period']), 'columns': ['time', 'demand'],
            'points': [[utc_timestamp, netload]]}
    influxdb.write_points([data])

@celery.task(name='tasks.energy.1h.aggregator')
def energy_1h_aggregate(user_id, meter_id):
    utc_now = datetime.utcfromtimestamp(time.time())
    tariff_data = get_tariff_details(user_id)

    energy_query = 'select mean(P) from "%s_%s" where time > now() - 1h;' % (user_id, meter_id)
    energy_query_result = influxdb.query(energy_query)
    energy = round(energy_query_result[0]['points'][0][1], 2)

    utc_timestamp = int((utc_now - datetime(1970, 1, 1)).total_seconds())
    data = {'name': '%s_%s_energy_1h_%s_%s' % (user_id, meter_id, tariff_data['season'], tariff_data['peak_period']), 'columns': ['time', 'energy_kwh'],
            'points': [[utc_timestamp, energy]]}
    influxdb.write_points([data])