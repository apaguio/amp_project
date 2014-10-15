from flask import request, Blueprint
from servers import r
from models import historical
from flask_login import login_required

historical_app = Blueprint('historical', __name__)

@historical_app.route("/historical/points/<start>/<end>", methods=["GET"])
@login_required
def historical_points(start, end):
    params = request.args
    solar_meter_id = 10068
    consumption_meter_id = 10054
    duration = params.get('timeframe', '10m')
    resolution = params.get('resolution', None)
    consumption = historical.get_ekm_data(consumption_meter_id, duration, resolution)
    solar = historical.get_ekm_data(solar_meter_id, duration, resolution)
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
    result = []
    return r.success(result)


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
    # TODO: SAVE TO DB
    return r.success(wrappers)

