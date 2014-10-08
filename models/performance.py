import time
from datetime import datetime
from models import db
from models.powerview import get_customer_timezone, get_tarrif_details
from models import influxdb
from pytz import timezone

def get_energy_data(meter_id):
    #used for both consumption and production
    result = dict()
    utc_now = datetime.utcfromtimestamp(time.time()) # current request time
    tarrif_data = get_tarrif_details(customer_name='test')
    customer_tz = timezone(tarrif_data['timezone'])
    customer_tz_now = customer_tz.fromutc(utc_now)
    time_diff = customer_tz_now - customer_tz.localize(datetime.strptime(tarrif_data['billing_period_startdate'], '%Y-%m-%d %H:%M:%S'))

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
    last_month_query_result = influxdb.query(last_month_query)
    energy_kwh_avgs = list()
    for res in last_month_query_result:
        energy_kwh_avgs.append(res['points'][0][1])
    if not energy_kwh_avgs:
        result['last_month'] = 0
    else:
        result['last_month'] = float(sum(energy_kwh_avgs))/len(energy_kwh_avgs) if len(energy_kwh_avgs) > 0 else float('nan')

    #last year query
    last_year_query = 'select mean(energy_kwh) from /^%s_energy_1h_\.*/ where time < now() - %sd and time > now() - %sd;' % (meter_id, time_diff.days, time_diff.days + 365)
    last_year_query_result = influxdb.query(last_year_query)
    energy_kwh_avgs = list()
    for res in last_year_query_result:
        energy_kwh_avgs.append(res['points'][0][1])
    if not energy_kwh_avgs:
        result['last_year'] = 0
    else:
        result['last_year'] = float(sum(energy_kwh_avgs))/len(energy_kwh_avgs) if len(energy_kwh_avgs) > 0 else float('nan')

    return result

def get_demand_data(meter_id):
    result = dict()
    utc_now = datetime.utcfromtimestamp(time.time()) # current request time
    tarrif_data = get_tarrif_details(customer_name='test') # TODO replace with current customer_id
    customer_tz = timezone(tarrif_data['timezone'])
    customer_tz_now = customer_tz.fromutc(utc_now)
    time_diff = customer_tz_now - customer_tz.localize(datetime.strptime(tarrif_data['billing_period_startdate'], '%Y-%m-%d %H:%M:%S'))

    #current billing period query
    billing_period_query = 'select max(demand) from /^%s_15mins_\.*/ where time > now() - %ss;' % (meter_id, time_diff.total_seconds())
    billing_period_query_result = influxdb.query(billing_period_query)
    demand_maxs = list()
    for res in billing_period_query_result:
        demand_maxs.append(res['points'][0][1])
    result['this_month'] = max(demand_maxs)

    #last month query
    last_month_query = 'select max(demand) from /^%s_15mins_\.*/ where time < now() - %sd and time > now() - %sd;' % (meter_id, time_diff.days, time_diff.days + 30)
    last_month_query_result = influxdb.query(last_month_query)
    demand_maxs = list()
    for res in last_month_query_result:
        demand_maxs.append(res['points'][0][1])
    if not demand_maxs:
        result['last_month'] = 0
    else:
        result['last_month'] = max(demand_maxs)

    #last year query
    last_year_query = 'select max(demand) from /^%s_15mins_\.*/ where time < now() - %sd and time > now() - %sd;' % (meter_id, time_diff.days, time_diff.days + 365)
    last_year_query_result = influxdb.query(last_year_query)
    demand_maxs = list()
    for res in last_year_query_result:
        demand_maxs.append(res['points'][0][1])
    if not demand_maxs:
        result['last_year'] = 0
    else:
        result['last_year'] = max(demand_maxs)

    return result

def calculate_energy_charges(meter_id):
    #can be used for both consumption and production
    utc_now = datetime.utcfromtimestamp(time.time()) # current request time
    tarrif_data = get_tarrif_details(customer_name='test') # TODO replace with current customer_id
    customer_tz = timezone(tarrif_data['timezone'])
    customer_tz_now = customer_tz.fromutc(utc_now)
    time_diff = customer_tz_now - customer_tz.localize(datetime.strptime(tarrif_data['billing_period_startdate'], '%Y-%m-%d %H:%M:%S'))

    energy_query = 'select sum(energy_kwh) from /^%s_energy_1h_\.*/ where time > now() - %ss;' % (meter_id, time_diff.total_seconds())
    energy_query_result = influxdb.query(energy_query)
    customer = db.Customer.objects(name='test').first()
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

def calculate_demand_charges(meter_id):
    utc_now = datetime.utcfromtimestamp(time.time()) # current request time
    tarrif_data = get_tarrif_details(customer_name='test') # TODO replace with current customer_id
    customer_tz = timezone(tarrif_data['timezone'])
    customer_tz_now = customer_tz.fromutc(utc_now)
    time_diff = customer_tz_now - customer_tz.localize(datetime.strptime(tarrif_data['billing_period_startdate'], '%Y-%m-%d %H:%M:%S'))

    demand_query = 'select max(demand) from /^%s_15mins_\.*/ where time > now() - %ss;' % (meter_id, time_diff.total_seconds())
    demand_query_result = influxdb.query(demand_query)
    customer = db.Customer.objects(name='test').first()
    demand_charges = 0.0
    demand_data = dict()
    for res in demand_query_result:
        name_parts = res['name'].split('_')
        season = name_parts[2]
        peakperiod = name_parts[3]
        for sn in customer['seasons']:
            if sn['name'] == season:
                if season not in demand_data:
                    demand_data[season] = list()
                demand_data[season].append(res['points'][0][1])
                for pp in sn['peak_periods']:
                    if pp['name'] == peakperiod:
                        if peakperiod == 'onpeak':
                            demand_charges += pp['demand_charge'] * res['points'][0][1]
                        else:
                            if pp['demand_charge'] not in demand_data[season]:
                                demand_data[season].append(pp['demand_charge'])
                        break
    for season, demand_values in demand_data.iteritems():
        max_demand_anytime = max(demand_values[:-1])
        demand_charges += max_demand_anytime * demand_values[-1]
    return demand_charges
