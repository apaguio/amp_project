from flask import Blueprint
from servers import r
from models import performance

performance_app = Blueprint('performance', __name__)

@performance_app.route("/performance/graph", methods=["GET"])
def performance_graph():
    solar_meter_id = 10068
    consumption_meter_id = 10054

    energy = performance.get_energy_data(consumption_meter_id)
    energy['this_month_money'] = performance.calculate_energy_charges(consumption_meter_id)
    energy['last_month_money'] = performance.calculate_energy_charges(consumption_meter_id)
    energy['last_year_money'] = performance.calculate_energy_charges(consumption_meter_id)

    solar = performance.get_energy_data(solar_meter_id)
    solar['this_month_money'] = performance.calculate_energy_charges(solar_meter_id)
    solar['last_month_money'] = performance.calculate_energy_charges(solar_meter_id)
    solar['last_year_money'] = performance.calculate_energy_charges(solar_meter_id)

    demand = performance.get_demand_data(consumption_meter_id)
    demand['this_month_money'] = performance.calculate_demand_charges(consumption_meter_id)
    demand['last_month_money'] = performance.calculate_demand_charges(consumption_meter_id)
    demand['last_year_money'] = performance.calculate_demand_charges(consumption_meter_id)

    res = {
        "energy": energy,
        "demand": demand,
        "solar": solar
    }
    print res
    return r.success(res)


@performance_app.route("/performance", methods=["GET"])
def performance_data():
    return r.success(performance.get_tariff_data())

