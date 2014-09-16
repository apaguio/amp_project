from app import app, r

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

