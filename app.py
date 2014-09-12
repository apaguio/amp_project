import json
from flask import Flask, Blueprint, abort, jsonify, request, session
import settings
import requests
from celery import Celery
from influxdb.client import InfluxDBClient
import xml.etree.ElementTree as ET
import datetime

app = Flask(__name__)
app.config.from_object(settings)

def make_celery(app):
    celery = Celery(app.import_name, broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)
    TaskBase = celery.Task
    class ContextTask(TaskBase):
        abstract = True
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery.Task = ContextTask
    return celery

def get_influxdb():
    db_name = 'cenergy_insights'
    client = InfluxDBClient()
    if db_name not in [db['name'] for db in client.get_database_list()]:
        client.create_database(db_name)
    client.switch_db(db_name)
    return client

celery = make_celery(app)
influxdb = get_influxdb()

@app.route("/test")
def hello_world(x=16, y=16):
    x = int(request.args.get("x", x))
    y = int(request.args.get("y", y))
    res = add.apply_async((x, y))
    context = {"id": res.task_id, "x": x, "y": y}
    result = "add((x){}, (y){})".format(context['x'], context['y'])
    goto = "{}".format(context['id'])
    return jsonify(body=result, goto=goto, result=res.get())

@celery.task(name="tasks.add")
def add(x, y):
    return x + y

@celery.task(name="tasks.ekm.collect")
def ekm_collect(meter_id, nr_readings, key, endpoint='io.ekmpush.com'):
    def _to_epoch(d):
        return (d - datetime.datetime(1970, 1, 1)).total_seconds()
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
        seq = _to_epoch(datetime.datetime.fromtimestamp(long(read.get('seq'))/1000) - datetime.timedelta(minutes=5))
        P = long(read.get('P')) # TODO: measured by W, to be converted to kW (i.e: /1000)
        L1_PF = _compute_pf(int(read.get('L1_PF')))
        L1_V = int(read.get('L1_V')) / 10
        data['points'].append([seq, P, L1_PF, L1_V])

    influxdb.write_points_with_precision(data, 'ms')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)