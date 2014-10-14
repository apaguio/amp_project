from flask import request, session, Blueprint
from servers import r
from models import diagnosis
from flask_login import login_required, current_user

diagnosis_app = Blueprint('diagnosis', __name__)

@diagnosis_app.route("/diagnosis/points/<start>/<end>", methods=["GET"])
@login_required
def diagnosis_points(start, end):
    consumption_meter_id = 10068
    solar_meter_id = 10054
    result = dict()
    result['consumption'] = diagnosis.get_ekm_data_range(consumption_meter_id, start, end)
    result['solar'] = diagnosis.get_ekm_data_range(solar_meter_id, start, end)
    return r.success(result)

@diagnosis_app.route("/diagnosis", methods=["GET"])
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


@diagnosis_app.route("/diagnosis", methods=["POST"])
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
