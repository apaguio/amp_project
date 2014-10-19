from flask import request, Blueprint
from servers import r
from models import historical
from flask_login import login_required, current_user

historical_app = Blueprint('historical', __name__)

@historical_app.route("/historical/points/<start>/<end>", methods=["GET"])
@login_required
def historical_points(start, end):
    params = request.args
    solar_meter_id = 10068
    consumption_meter_id = 10054
    resolution = params.get('resolution', None)
    consumption = historical.get_ekm_data(consumption_meter_id, start, end, resolution)
    solar = historical.get_ekm_data(solar_meter_id, start, end, resolution)
    solarLen = len(solar)
    for i, d in enumerate(consumption):
        if i < solarLen:
            d['S'] = solar[i].get('P', 0)
    # Return consumption after updating with solar
    # NOTE: assumption that S has the same timestamp as P
    consumption = sorted(consumption, key=lambda k: k['time'])
    return r.success(consumption)

@historical_app.route("/historical", methods=["GET"])
@login_required
def get_historical_instances():
    """ Based on customer_id we should return the last state of historical tab
        this should return array of wrappers each one has its own config.
        wrappers: [
            {
                start: date,
                end: date,
                zoom_start: timestamp,
                zoom_end timestamp,
                graph: string
            }
        ]
    """
    return r.success(current_user.historicals or [])


@historical_app.route("/historical", methods=["POST"])
@login_required
def set_historical_instances():
    """ Based on customer_id we should return the last state of historical tab
        this should return array of wrappers each one has its own config.
        wrappers: [
            {
                start: date,
                end: date,
                zoom_start: timestamp,
                zoom_end timestamp,
                graph: string
            }
        ]
    """
    wrappers = request.json
    current_user.historicals = wrappers
    current_user.save();
    return r.success(wrappers)

@historical_app.route("/historical/<id>", methods=["POST"])
@login_required
def update_historical_instance():
    """ Based on customer_id we should return the last state of historical tab
        this should return array of wrappers each one has its own config.
        wrappers: [
            {
                start: date,
                end: date,
                zoom_start: timestamp,
                zoom_end timestamp,
                graph: string
            }
        ]
    """
    #current_user.historicals = db.historical.get("")
    wrappers = request.json
    return r.success(wrappers)
