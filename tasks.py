import requests
import time
from app import celery
from celery.utils.log import get_task_logger
import xml.etree.ElementTree as ET
from influxdb_factory import get_influxdb
from datetime import datetime
from redis import Redis
from models import powerview

influxdb = get_influxdb()
logger = get_task_logger(__name__)
redis = Redis()

@celery.task(name="tasks.ekm.collect")
def ekm_collect(meter_id, nr_readings, key, endpoint='io.ekmpush.com', simulate_solar=False):
    logger.info('executing task: "ekm_collect" with args: meter_id:%s, nr_readings:%s, key:%s' %
                (meter_id, nr_readings, key))
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
    root = ET.fromstring(ekm_data)
    for read in root.iter('read'):
        seq = (long(read.get('seq'))/1000) - 300 # -300 seconds, fix ekm bug +5 mins
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

@celery.task(name='tasks.ekm.facility.15mins.aggregator')
def ekm_facility_aggregate(meter_id, solar_meter_id):
    utc_now = datetime.utcfromtimestamp(time.time())
    # get user information (customer_id) from session
    tarrif_data = powerview.get_tarrif_details(customer_name='test')

    facility_query = 'select mean(P) as demand from "%s" group by time(15m) limit 1;' % meter_id
    facility_result = influxdb.query(facility_query)
    demand = round(facility_result[0]['points'][0][1], 2)

    solar_power = 0
    solar_query = 'select mean(P) as demand from "%s" group by time(15m) limit 1;' % solar_meter_id
    solar_result = influxdb.query(solar_query)
    if solar_result:
        solar_power = round(solar_result[0]['points'][0][1], 2)
    net_load = demand - solar_power

    utc_timestamp = int((utc_now - datetime(1970, 1, 1)).total_seconds())
    data = {'name': '%s_15mins_%s' % (meter_id, tarrif_data['peak_period']), 'columns': ['time', 'demand'], 
            'points': [[utc_timestamp, net_load]]}
    influxdb.write_points([data])