from flask import Blueprint
from servers import r
from models import performance
from models.utils import get_tariff_data
from flask_login import login_required

performance_app = Blueprint('performance', __name__)

@performance_app.route("/performance/graph", methods=["GET"])
@login_required
def performance_graph():
    solar_meter_id = 10068
    consumption_meter_id = 10054

    energy = performance.get_energy_data(consumption_meter_id)
    energy['charges'] = performance.calculate_energy_charges(consumption_meter_id)

    solar = performance.get_energy_data(solar_meter_id)
    solar['charges'] = performance.calculate_energy_charges(solar_meter_id)

    demand = performance.get_demand_data(consumption_meter_id)
    demand['charges'] = performance.calculate_demand_charges(consumption_meter_id)

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
    return r.success(get_tariff_data())

