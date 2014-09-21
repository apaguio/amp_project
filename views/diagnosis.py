from socketio.mixins import RoomsMixin, BroadcastMixin
from werkzeug.exceptions import NotFound
from gevent import monkey
from app import r, app, pubsub
from models import diagnosis

@app.route("/diagnosis/points/<start>/<end>", methods=["GET"])
def diagnosis_points(start, end):
    consumption_meter_id = 10068
    solar_meter_id = 10054
    result = dict()
    result['consumption'] = diagnosis.get_ekm_data_range(consumption_meter_id, start, end)
    result['solar'] = diagnosis.get_ekm_data_range(solar_meter_id, start, end)
    return r.success(result)