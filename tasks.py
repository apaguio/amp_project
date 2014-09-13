import settings
import requests
from datetime import datetime, timedelta
from celery import Celery
import xml.etree.ElementTree as ET
from influxdb_factory import get_influxdb

celery = Celery('cenergy_insights')
celery.config_from_object('settings')
influxdb = get_influxdb()

@celery.task
def add(x, y):
    return x + y

@celery.task(name="tasks.ekm.collect")
def ekm_collect(meter_id, nr_readings, key, endpoint='io.ekmpush.com'):
    def _to_epoch(d):
        return (d - datetime(1970, 1, 1)).total_seconds()
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
        seq = _to_epoch(datetime.fromtimestamp(long(read.get('seq'))/1000) - timedelta(minutes=5))
        P = long(read.get('P')) # TODO: measured by W, to be converted to kW (i.e: /1000)
        L1_PF = _compute_pf(int(read.get('L1_PF')))
        L1_V = int(read.get('L1_V')) / 10
        data['points'].append([seq, P, L1_PF, L1_V])

    influxdb.write_points_with_precision(data, 'ms')