from flask import request, session, Blueprint
from servers import r
from models import historical
from flask_login import login_required

historical_app = Blueprint('historical', __name__)

@historical_app.route("/historical/points/<start>/<end>", methods=["GET"])
@login_required
def historical_points(start, end):
    consumption_meter_id = 10068
    solar_meter_id = 10054
    result = dict()
    result['consumption'] = historical.get_ekm_data_range(consumption_meter_id, start, end)
    result['solar'] = historical.get_ekm_data_range(solar_meter_id, start, end)
    return r.success(result)

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
def set_historical_instances(configs):
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

