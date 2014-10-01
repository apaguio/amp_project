from flask import Blueprint
from servers import r

performance_app = Blueprint('performance', __name__)

@performance_app.route("/performance/graph", methods=["GET"])
def performance_graph():
    return r.success({
        "energy": {
            "this_month" : 23000,
            "last_month" : 12000,
            "last_year" : 240000
        },
        "demand": {
            "this_month" : 23000,
            "last_month" : 12000,
            "last_year" : 240000
        },
        "solar": {
            "this_month" : 12000,
            "last_month" : 23000,
            "last_year" : 0
        }
    })


@performance_app.route("/performance", methods=["GET"])
def performance():
    return r.success({
        "billing_period": "september",
        "billing_period_startdate": 1410380825,
        "billing_period_enddate": 1410380825,
        "season": "summer",
        "season_startdate": 1410380825,
        "season_enddate": 1410380825,
        "tariff": "AG-5E"
    })

