from flask import Response, request
from socketio import socketio_manage
from socketio.namespace import BaseNamespace
from socketio.mixins import RoomsMixin, BroadcastMixin
from werkzeug.exceptions import NotFound
from gevent import monkey
from app import r, app, pubsub


@app.route("/powerview", methods=["POST"])
def powerview():
    return r.success({
        "billing_period": "september",
        "billing_period_startdate": 1410380825,
        "billing_period_enddate": 1410380825,
        "season": "summer",
        "season_startdate": 1410380825,
        "season_enddate": 1410380825,
        "period": "peak",
        "energy_charge": 0.19,
        "demand_charge": 21.46,
        "current_demand": 1254,
        "current_demand_startdate": 1410380825,
        "current_demand_enddate": 1410380825,
        "max_demand": 1455,
        "max_demand_startdate": 1410380825,
        "max_demand_enddate": 1410380825,
        "power_factor": 0.9
    })


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
