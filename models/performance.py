import time
from datetime import datetime
from models import db
from models.powerview import get_tariff_details
from models import influxdb
from pytz import timezone
from flask_login import current_user

def get_energy_data(meter_id):
    #used for both consumption and production
    result = dict()
    utc_now = datetime.utcfromtimestamp(time.time()) # current request time
    tariff_data = get_tariff_details()
    customer_tz = timezone(tariff_data['timezone'])
    customer_tz_now = customer_tz.fromutc(utc_now)
    time_diff = customer_tz_now - customer_tz.localize(datetime.strptime(tariff_data['billing_period_startdate'], '%Y-%m-%d %H:%M:%S'))

    #current billing period query
    billing_period_query = 'select mean(energy_kwh) from /^%s_energy_1h_\.*/ where time > now() - %ss;' % (meter_id, time_diff.total_seconds())
    print billing_period_query
    # until merge('%s_energy_1h_*') with regex works
    billing_period_query_result = influxdb.query(billing_period_query)
    energy_kwh_avgs = list()
    for res in billing_period_query_result:
        energy_kwh_avgs.append(res['points'][0][1])
    if not energy_kwh_avgs:
        result['this_month'] = 0
    else:
        result['this_month'] = float(sum(energy_kwh_avgs))/len(energy_kwh_avgs) if len(energy_kwh_avgs) > 0 else float('nan')

    #last month query
    last_month_query = 'select mean(energy_kwh) from /^%s_energy_1h_\.*/ where time < now() - %sd and time > now() - %sd;' % (meter_id, time_diff.days, time_diff.days + 30)
    try:
        last_month_query_result = influxdb.query(last_month_query)
        energy_kwh_avgs = list()
        for res in last_month_query_result:
            energy_kwh_avgs.append(res['points'][0][1])
        if not energy_kwh_avgs:
            result['last_month'] = 0
        else:
            result['last_month'] = float(sum(energy_kwh_avgs))/len(energy_kwh_avgs) if len(energy_kwh_avgs) > 0 else float('nan')
    except:
        result['last_month'] = 0

    #last year query
    last_year_query = 'select mean(energy_kwh) from /^%s_energy_1h_\.*/ where time < now() - %sd and time > now() - %sd;' % (meter_id, time_diff.days + 365, time_diff.days + 365 + 30)
    try:
        last_year_query_result = influxdb.query(last_year_query)
        energy_kwh_avgs = list()
        for res in last_year_query_result:
            energy_kwh_avgs.append(res['points'][0][1])
        if not energy_kwh_avgs:
            result['last_year'] = 0
        else:
            result['last_year'] = float(sum(energy_kwh_avgs))/len(energy_kwh_avgs) if len(energy_kwh_avgs) > 0 else float('nan')
    except:
        result['last_year'] = 0
    return result

def get_demand_data(meter_id):
    result = dict()
    utc_now = datetime.utcfromtimestamp(time.time()) # current request time
    tariff_data = get_tariff_details()
    customer_tz = timezone(tariff_data['timezone'])
    customer_tz_now = customer_tz.fromutc(utc_now)
    time_diff = customer_tz_now - customer_tz.localize(datetime.strptime(tariff_data['billing_period_startdate'], '%Y-%m-%d %H:%M:%S'))

    #current billing period query
    billing_period_query = 'select max(demand) from /^%s_15mins_\.*/ where time > now() - %ss;' % (meter_id, time_diff.total_seconds())
    billing_period_query_result = influxdb.query(billing_period_query)
    demand_maxs = list()
    for res in billing_period_query_result:
        demand_maxs.append(res['points'][0][1])
    result['this_month'] = max(demand_maxs)

    #last month query
    last_month_query = 'select max(demand) from /^%s_15mins_\.*/ where time < now() - %sd and time > now() - %sd;' % (meter_id, time_diff.days, time_diff.days + 30)
    try:
        last_month_query_result = influxdb.query(last_month_query)
        demand_maxs = list()
        for res in last_month_query_result:
            demand_maxs.append(res['points'][0][1])
        if not demand_maxs:
            result['last_month'] = 0
        else:
            result['last_month'] = max(demand_maxs)
    except:
        result['last_month'] = 0

    #last year query
    last_year_query = 'select max(demand) from /^%s_15mins_\.*/ where time < now() - %sd and time > now() - %sd;' % (meter_id, time_diff.days + 365, time_diff.days + 365 + 30)
    try:
        last_year_query_result = influxdb.query(last_year_query)
        demand_maxs = list()
        for res in last_year_query_result:
            demand_maxs.append(res['points'][0][1])
        if not demand_maxs:
            result['last_year'] = 0
        else:
            result['last_year'] = max(demand_maxs)
    except:
        result['last_year'] = 0
    return result

def _calculate_energy_charges_helper(energy_query_result):
    customer = current_user
    energy_charges = 0.0
    for res in energy_query_result:
        name_parts = res['name'].split('_')
        season = name_parts[3]
        peakperiod = name_parts[4]
        for sn in customer['seasons']:
            if sn['name'] == season:
                for pp in sn['peak_periods']:
                    if pp['name'] == peakperiod:
                        energy_charges += pp['energy_charge'] * res['points'][0][1]
                        break
    return energy_charges

def calculate_energy_charges(meter_id):
    #can be used for both consumption and production
    result = dict()
    utc_now = datetime.utcfromtimestamp(time.time()) # current request time
    tariff_data = get_tariff_details()
    customer_tz = timezone(tariff_data['timezone'])
    customer_tz_now = customer_tz.fromutc(utc_now)
    time_diff = customer_tz_now - customer_tz.localize(datetime.strptime(tariff_data['billing_period_startdate'], '%Y-%m-%d %H:%M:%S'))

    #current billing period query
    energy_query = 'select sum(energy_kwh) from /^%s_energy_1h_\.*/ where time > now() - %ss;' % (meter_id, time_diff.total_seconds())
    energy_query_result = influxdb.query(energy_query)
    result['this_month'] = _calculate_energy_charges_helper(energy_query_result)

    #last month query
    last_month_energy_query = 'select sum(energy_kwh) from /^%s_energy_1h_\.*/ where time < now() - %sd and time > now() - %sd;' % (meter_id, time_diff.days, time_diff.days + 30)
    try:
        last_month_energy_query_result = influxdb.query(last_month_energy_query)
        result['last_month'] = _calculate_energy_charges_helper(last_month_energy_query_result)
    except:
        result['last_month'] = 0

    #last year query
    last_year_energy_query = 'select sum(energy_kwh) from /^%s_energy_1h_\.*/ where time < now() - %sd and time > now() - %sd;' % (meter_id, time_diff.days + 365, time_diff.days + 365 + 30)
    try:
        last_year_energy_query_result = influxdb.query(last_year_energy_query)
        result['last_year'] = _calculate_energy_charges_helper(last_year_energy_query_result)
    except:
        result['last_year'] = 0
    return result

def _calculate_demand_charges_helper(demand_query_result):
    customer = current_user
    total_demand_charges = 0.0
    demand_data = dict()
    demand_charges = dict()
    for res in demand_query_result:
        max_demand = res['points'][0][1]
        name_parts = res['name'].split('_')
        peakperiod = name_parts[3]
        season = name_parts[2]
        if season not in demand_data:
            demand_data[season] = list()
        for sn in customer['seasons']:
            if sn['name'] != season:
                continue
            demand_data[season].append(max_demand)
            for pp in sn['peak_periods']:
                if pp['name'] != peakperiod:
                    continue
                if peakperiod == 'onpeak':
                    total_demand_charges += pp['demand_charge'] * max_demand
                else:
                    demand_charges[season] = pp['demand_charge']
    for season, demand_values in demand_data.iteritems():
        max_demand_anytime = max(demand_values)
        total_demand_charges += max_demand_anytime * demand_charges[season]
    return total_demand_charges

def calculate_demand_charges(meter_id):
    result = dict()
    utc_now = datetime.utcfromtimestamp(time.time()) # current request time
    tariff_data = get_tariff_details()
    customer_tz = timezone(tariff_data['timezone'])
    customer_tz_now = customer_tz.fromutc(utc_now)
    time_diff = customer_tz_now - customer_tz.localize(datetime.strptime(tariff_data['billing_period_startdate'], '%Y-%m-%d %H:%M:%S'))

    # current billing period query
    demand_query = 'select max(demand) from /^%s_15mins_\.*/ where time > now() - %ss;' % (meter_id, time_diff.total_seconds())
    demand_query_result = influxdb.query(demand_query)
    result['this_month'] = _calculate_demand_charges_helper(demand_query_result)

    # last month query
    last_month_demand_query = 'select max(demand) from /^%s_15mins_\.*/ where time < now() - %sd and time > now() - %sd;' % (meter_id, time_diff.days, time_diff.days + 30)
    try:
        last_month_demand_query_result = influxdb.query(last_month_demand_query)
        result['last_month'] = _calculate_demand_charges_helper(last_month_demand_query_result)
    except:
        result['last_month'] = 0

    # last year query
    last_year_demand_query = 'select max(demand) from /^%s_15mins_\.*/ where time < now() - %sd and time > now() - %sd;' % (meter_id, time_diff.days + 365, time_diff.days + 365 + 30)
    try:
        last_year_demand_query_result = influxdb.query(last_year_demand_query)
        result['last_year'] = _calculate_demand_charges_helper(last_year_demand_query_result)
    except:
        result['last_year'] = 0
    return result

def get_tariff_data():
    return get_tariff_details()
