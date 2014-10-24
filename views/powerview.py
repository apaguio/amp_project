from flask import Blueprint, Response, request
from socketio import socketio_manage
from socketio.namespace import BaseNamespace
from socketio.mixins import RoomsMixin, BroadcastMixin
from servers import r, pubsub
from models import powerview, utils
from flask_login import login_required

powerview_app = Blueprint('powerview', __name__)

# TODO: to be removed or moved to a deveopment based blueprint
@powerview_app.route("/demo_data/generate", methods=["GET"])
def generate_demo_data():
    utils.generate_demo_data()
    result = {'result': True}
    return r.success(result)

@powerview_app.route("/powerview/points", methods=["GET"])
@login_required
def powerview_points():
    params = request.args
    solar_meter_id = 10068
    consumption_meter_id = 10054
    duration = params.get('timeframe', '10m')
    resolution = params.get('resolution', None)
    consumption = powerview.get_ekm_data(consumption_meter_id, duration, resolution)
    solar = powerview.get_ekm_data(solar_meter_id, duration, resolution)
    solarLen = len(solar)
    for i, d in enumerate(consumption):
        if i < solarLen:
            d['S'] = solar[i].get('P', 0)
    # Return consumption after updating with solar
    # NOTE: assumption that S has the same timestamp as P
    consumption = sorted(consumption, key=lambda k: k['time'])
    return r.success(consumption)

@powerview_app.route("/powerview/current_demand", methods=["GET"])
@login_required
def get_current_demand():
    consumption_meter_id = 10054
    solar_meter_id = 10068
    result = powerview.get_current_demand(consumption_meter_id, solar_meter_id)
    return r.success(result)

@powerview_app.route("/powerview/max_peak_demand", methods=["GET"])
@login_required
def get_max_peak_demand():
    consumption_meter_id = 10054
    result = powerview.get_max_peak_demand(consumption_meter_id)
    return r.success(result)

@powerview_app.route("/powerview/max_demand_anytime", methods=["GET"])
@login_required
def get_max_demand_anytime():
    consumption_meter_id = 10054
    result = powerview.get_max_demand_anytime(consumption_meter_id)
    return r.success(result)

@powerview_app.route("/powerview", methods=["GET"])
@login_required
def powerview_data():
    return r.success(utils.get_tariff_details())

class PowerViewNS(BaseNamespace, RoomsMixin, BroadcastMixin):

    data = []

    def initialize(self):
        #self.logger = app.logger
        self.log("Socketio session started")
        points = pubsub.subscribe(['point'])
        for point in points:
            self.broadcast_event('point', point)

@powerview_app.route('/socket.io/<path:remaining>')
def socketio(remaining):
    try:
        socketio_manage(request.environ, {'/powerview': PowerViewNS}, request)
    except:
        pass
        #app.logger.error("Exception while handling socketio connection", exc_info=True)
    return Response()
