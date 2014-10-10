from flask import Blueprint
from servers import r
from models import performance

performance_app = Blueprint('performance', __name__)

@performance_app.route("/performance/graph", methods=["GET"])
def performance_graph():
    solar_meter_id = 10068
    consumption_meter_id = 10054
    energy_consumption_kwh = performance.get_energy_data(consumption_meter_id)
    solar_production_kwh = performance.get_energy_data(solar_meter_id)
    demand = performance.get_demand_data(consumption_meter_id)
    res = {
        "energy": energy_consumption_kwh,
        "demand": demand,
        "solar": solar_production_kwh
    }
    print res
    return r.success(res)


@performance_app.route("/performance", methods=["GET"])
def performance_data():
    return r.success(performance.get_tariff_data())

