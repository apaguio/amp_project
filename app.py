from flask_settings import *
from gevent import monkey
from socketio.server import SocketIOServer
from flask import Flask, Blueprint, abort, jsonify, request, session
from influxdb_factory import get_influxdb
from flask.ext.pymongo import PyMongo
from helpers import CreateResponse
import redis

app = Flask(__name__)
app.config.from_object('flask_settings')
app.secret_key = "somesecretkey77"
influxdb = get_influxdb()
mongodb = PyMongo(app)
# Building the Response instance that is used to form the json structure
redisServer = redis.Redis()
pubsub = redisServer.pubsub()
r = CreateResponse()

@app.route('/tarrif/<name>')
def get_tarrif_details(name):
    # later on, can be extended by periods
    result = mongodb.db.tarrif.find_one({'name': name}, fields={'_id': False}) or list()
    return jsonify(result)

@app.route('/ekm_data_one_second/<meter_id>/<int:duration_in_seconds>')
def get_ekm_data_one_sec_intervals(meter_id, duration_in_seconds):
    query = 'select * from "%s" where time > now() - %ss' % (meter_id, duration_in_seconds)
    result = influxdb.query(query)
    if result:
        return jsonify(result[0])
    else:
        return jsonify(result)

@app.route('/current_demand/<meter_id>')
def get_current_demand(meter_id):
    query = 'select mean(P) as current_demand from "%s" group by time(15m) limit 1' % meter_id
    result = influxdb.query(query)
    if result:
        return jsonify(result[0]['points'][0][1])
    else:
        return jsonify(result)


from views.performance import *
from views.powerview import *

monkey.patch_all()

PORT = 5000
SOCKETIOPORT = 5001

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=PORT)
    SocketIOServer(('', SOCKETIOPORT), app, resource="socket.io").serve_forever()

