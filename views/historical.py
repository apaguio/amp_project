from flask import request, Blueprint
from servers import r
from models import historical, db
from flask_login import login_required, current_user
from uuid import uuid4

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
                resolution: string,
                zoom_start: timestamp,
                zoom_end timestamp,
                graph: string
            }
        ]
    """
    user = db.Customer.objects(id=current_user.get_id()).first()
    return r.success(user.historicals or [])


@historical_app.route("/historical", methods=["POST"])
@login_required
def set_historical_instances():
    """ Based on customer_id we should return the last state of historical tab
        this should return array of wrappers each one has its own config.
        wrappers: [
            {
                start: date,
                end: date,
                resolution: string,
                zoom_start: timestamp,
                zoom_end timestamp,
                graph: string
            }
        ]
    """
    wrappers = request.json
    user = db.Customer.objects(id=current_user.get_id()).first()
    user.historicals = []
    for wrapper in wrappers:
        wrapper['zoom_start'] = wrapper.get('zoom_start', wrapper.get('start'))
        wrapper['zoom_end'] = wrapper.get('zoom_end', wrapper.get('end'))
        graphs = wrapper.get('graphs', {})
        wrapper['graphs'] = []
        for graph, visible in graphs.iteritems():
            if visible:
                wrapper['graphs'].append(graph)
        wrapper['id'] = str(uuid4())
        historical = db.Historical(**wrapper)
        user.historicals.append(historical)
    user.save();
    return r.success(wrappers)

@historical_app.route("/historical/<id>", methods=["POST"])
@login_required
def update_historical_instance(id):
    """ Based on customer_id we should return the last state of historical tab
        this should return array of wrappers each one has its own config.
        wrappers: [
            {
                start: date,
                end: date,
                resolution: string,
                zoom_start: timestamp,
                zoom_end timestamp,
                graph: string
            }
        ]
    """
    wrapper = request.json
    user = db.Customer.objects(id=current_user.get_id()).first()
    index = -1
    for i, h in enumerate(user.historicals):
        if h.id == id:
            index = i
            break

    wrapper['id'] = id
    wrapper['zoom_start'] = wrapper.get('zoom_start', wrapper.get('start'))
    wrapper['zoom_end'] = wrapper.get('zoom_end', wrapper.get('end'))
    graphs = wrapper.get('graphs', {})
    wrapper['graphs'] = []
    for graph, visible in graphs.iteritems():
        if visible:
            wrapper['graphs'].append(graph)
    historical = db.Historical(**wrapper)
    if index >= 0:
        user.historicals[index] = historical
    else:
        user.historicals.append(historical)
    user.save()
    return r.success(historical)

@historical_app.route("/historical/<id>", methods=["DELETE"])
@login_required
def remove_historical_instance(id):
    print "Deleteing %s" % id
    user = db.Customer.objects(id=current_user.get_id()).first()
    index = -1
    for i, h in enumerate(user.historicals):
        if h.id == id:
            index = i
            break

    print index
    if index >= 0:
        del user.historicals[index]
        user.save()
        return r.success()
    return r.error()
