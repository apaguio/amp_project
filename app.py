from flask_settings import *
from flask import Flask, Blueprint, abort, jsonify, request, session
from influxdb_factory import get_influxdb
from flask.ext.pymongo import PyMongo
from helpers import CreateResponse

app = Flask(__name__)
app.config.from_object('flask_settings')
app.secret_key = "somesecretkey77"
influxdb = get_influxdb()
mongodb = PyMongo(app)
# Building the Response instance that is used to form the json structure
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

@app.route("/logout", methods=["POST"])
def logout():
    session['logged_in'] = False
    return r.success()

@app.route("/login", methods=["POST"])
def login():
    credentials = request.json
    if credentials['username'] != 'test' or credentials['password'] != 'test':
        error = 'Invalid username or password'
        return r.error(error)
    else:
        session['logged_in'] = True
        # TODO: Updaate user_id & user_roel from db
        return r.success({
            "session_id": session.get('_id'),
            "user_id": 2,
            "user_role": "user",
            "csrf_token": session.get('csrf_token')
        })

@app.route("/performance", methods=["POST"])
def performance():
    return r.success({
        "billing_period": "september",
        "billing_period_startdate": 1410380825,
        "billing_period_enddate": 1410380825,
        "season": "summer",
        "season_startdate": 1410380825,
        "season_enddate": 1410380825,
        "tariff": "AG-5E"
    })

@app.route("/powerview", methods=["POST"])
def powerview():
    return r.success({
        "billing_period": "september",
        "billing_period_startdate": 1410380825,
        "billing_period_enddate": 1410380825,
        "season": "summer",
        "season_startdate": 1410380825,
        "season_enddate": 1410380825,
        "period": "peak",
        "energy_charge": 0.19,
        "demand_charge": 21.46,
        "current_demand": 1254,
        "current_demand_startdate": 1410380825,
        "current_demand_enddate": 1410380825,
        "max_demand": 1455,
        "max_demand_startdate": 1410380825,
        "max_demand_enddate": 1410380825,
        "power_factor": 0.9
    })


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
