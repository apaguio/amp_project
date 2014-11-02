from flask import Blueprint
from servers import r
from models import performance
from models.utils import get_tariff_details
from flask_login import login_required, current_user

performance_app = Blueprint('performance', __name__)

@performance_app.route("/performance/graph", methods=["GET"])
@login_required
def performance_graph():
    for meter in current_user.facility:
        energy = performance.get_energy_data(meter.id)
        energy['charges'] = performance.calculate_energy_charges(meter.id)
    for meter in current_user.solar:
        solar = performance.get_energy_data(meter.id)
        solar['charges'] = performance.calculate_energy_charges(meter.id)

    demand = performance.get_demand_data()
    demand['charges'] = performance.calculate_demand_charges()
    demand['charges']['this_month'] = demand['charges']['this_month']/ 30
    demand['charges']['last_month'] = demand['charges']['last_month'] / 30
    demand['charges']['last_year'] = demand['charges']['last_year'] / 30

    res = {
        "energy": energy,
        "demand": demand,
        "solar": solar
    }
    return r.success(res)


@performance_app.route("/performance", methods=["GET"])
@login_required
def performance_data():
    return r.success(get_tariff_details())

