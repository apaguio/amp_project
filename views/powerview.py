from flask import Response, request
from socketio import socketio_manage
from socketio.namespace import BaseNamespace
from socketio.mixins import RoomsMixin, BroadcastMixin
from werkzeug.exceptions import NotFound
from gevent import monkey
from app import r, app, pubsub
from models import powerview

@app.route("/demo_data/generate", methods=["GET"])
def generate_demo_data():
    powerview.generate_demo_data()
    result = {'result': True}
    return r.success(result)

@app.route("/powerview/points", methods=["GET"])
def powerview_points():
    consumption_meter_id = 10068
    solar_meter_id = 10054
    duration = '5d'
    result = dict()
    result['consumption'] = powerview.get_ekm_data(consumption_meter_id, duration)
    result['solar'] = powerview.get_ekm_data(solar_meter_id, duration)
    return r.success(result)

@app.route("/powerview/current_demand", methods=["GET"])
def get_current_demand():
    result = dict()
    consumption_meter_id = 10054
    result['current_demand'] = powerview.get_current_demand(consumption_meter_id)
    return r.success(result)

@app.route("/powerview/max_demand", methods=["GET"])
def get_max_demand():
    result = dict()
    consumption_meter_id = 10054
    result['max_demand'] = powerview.get_max_demand(consumption_meter_id)
    return r.success(result)

@app.route("/powerview", methods=["GET"])
def powerview_data():
    return r.success(powerview.get_tarrif_details())

class PowerViewNS(BaseNamespace, RoomsMixin, BroadcastMixin):

    data = []

    def initialize(self):
        self.logger = app.logger
        self.log("Socketio session started")
        points = pubsub.subscribe(['point'])
        for point in points:
            self.broadcast_event('point', point)

@app.route('/socket.io/<path:remaining>')
def socketio(remaining):
    try:
        socketio_manage(request.environ, {'/powerview': PowerViewNS}, request)
    except:
        app.logger.error("Exception while handling socketio connection",
                         exc_info=True)
    return Response()
