from flask import Blueprint, Response, request
from servers import r
from models import powerview, utils
from flask_login import login_required, current_user

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
    duration = params.get('timeframe', '10m')
    resolution = params.get('resolution', None)
    for meter in current_user.facility:
        consumption = powerview.get_ekm_data(meter.id, duration, resolution)
    for meter in current_user.solar:
        solar = powerview.get_ekm_data(meter.id, duration, resolution)
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