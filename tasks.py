import requests
from celery import Celery
from celery.utils.log import get_task_logger
import xml.etree.ElementTree as ET
from influxdb_factory import get_influxdb
from app import redisSrever

celery = Celery('cenergy_insights')
celery.config_from_object('celery_settings')
influxdb = get_influxdb()
logger = get_task_logger(__name__)

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
        P = long(read.get('P')) # TODO: measured by W, to be converted to kW (i.e: /1000)
        if simulate_solar:
            P = P / 3
        L1_PF = _compute_pf(int(read.get('L1_PF')))
        L1_V = int(read.get('L1_V')) / 10
        data['points'].append([seq, P, L1_PF, L1_V])

    # Publishing to pubsub when event occurs, to be sent by socket.io
    publishMsg = {"meter_id": meter_id, "point": [seq, P, L1_PF, L1_V]}
    redisSrever.publish('point', publishMsg)

    # Write to timeseries db
    influxdb.write_points([data])
