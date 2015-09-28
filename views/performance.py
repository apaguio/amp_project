from flask import Blueprint
from servers import r
from models import performance
from models.utils import get_tariff_details
from flask_login import login_required
from meter_settings import SOLAR_METER_ID, CONSUMPTION_METER_ID

performance_app = Blueprint('performance', __name__)

@performance_app.route("/performance/graph", methods=["GET"])
@login_required
def performance_graph():
    energy = performance.get_energy_data(CONSUMPTION_METER_ID)
    energy['charges'] = performance.calculate_energy_charges(CONSUMPTION_METER_ID)

    solar = performance.get_energy_data(SOLAR_METER_ID)
    solar['charges'] = performance.calculate_energy_charges(SOLAR_METER_ID)

    demand = performance.get_demand_data(CONSUMPTION_METER_ID)
    demand['charges'] = performance.calculate_demand_charges(CONSUMPTION_METER_ID)
    demand['charges']['this_month'] = demand['charges']['this_month']/ 30
    demand['charges']['last_month'] = demand['charges']['last_month'] / 30
    demand['charges']['last_year'] = demand['charges']['last_year'] / 30

    res = {
        "energy": energy,
        "demand": demand,
        "solar": solar
    }
    print res
    return r.success(res)


@performance_app.route("/performance", methods=["GET"])
@login_required
def performance_data():
    return r.success(get_tariff_details())

