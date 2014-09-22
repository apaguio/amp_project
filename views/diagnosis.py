from flask import Blueprint
from servers import r
from models import diagnosis

diagnosis_app = Blueprint('diagnosis', __name__)

@diagnosis_app.route("/diagnosis/points/<start>/<end>", methods=["GET"])
def diagnosis_points(start, end):
    consumption_meter_id = 10068
    solar_meter_id = 10054
    result = dict()
    result['consumption'] = diagnosis.get_ekm_data_range(consumption_meter_id, start, end)
    result['solar'] = diagnosis.get_ekm_data_range(solar_meter_id, start, end)
    return r.success(result)
