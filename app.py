from flask_settings import *
from flask import Flask, Blueprint, abort, jsonify, request, session
from influxdb_factory import get_influxdb
from flask.ext.pymongo import PyMongo
from tasks import add

app = Flask(__name__)
app.config.from_object('flask_settings')
influxdb = get_influxdb()
mongodb = PyMongo(app)

@app.route('/tarrif/<name>')
def get_tarrif_details(name):
    # later on, can be extended by periods
    result = mongodb.db.tarrif.find_one({'name': name}, fields={'_id': False}) or list()
    return jsonify(result)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)