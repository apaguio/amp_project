from flask import Blueprint
from servers import r

performance_app = Blueprint('performance', __name__)

@performance_app.route("/performance", methods=["POST"])
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

