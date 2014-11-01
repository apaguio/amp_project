import time
from datetime import datetime
from models import db, influxdb, utils
from pytz import timezone
from flask_login import current_user

def get_ekm_data(meter_id, period, resolution=None):
    """
    Gets EKM Data
    @parm meter_id   currently ( 10068 - consumption, 10054 - solar )
    @parm period     time window in appended by time letter ( s - seconds, m - minutes, h - hours, d - days)
    @parm resolution data resolution, i.e aggregation interval, same format as period, like: 1m, 5m, etc
          leave it None (default) to get 1s resolution, i.e all data available (large data sets)
    """
    acceptable_resolution = utils.is_acceptable_resolution(resolution)
    if not resolution or resolution == '1s':
        query = 'select P, L1_PF, L1_V from "%s_%s" where time > now() - %s;' % (current_user.get_id(), meter_id, period)
    else:
        if acceptable_resolution:
            query = '''select P, L1_PF, L1_V
                    from "%s_%s_%s" where time > now() - %s;''' % (current_user.get_id(), meter_id, acceptable_resolution, period)
        else:
            query = '''select mean(P) as P, mean(L1_PF) as L1_PF, mean(L1_V) as L1_V
                    from "%s_%s" where time > now() - %s group by time(%s);''' % (current_user.get_id(), meter_id, period, resolution)
    return utils.collect_ekm_data(query)

def _get_power_avg(meter_id, number_of_miutes, utc_now):
    query = 'select mean(P) from "%s_%s" where time > now() - %ss;' % (current_user.get_id(), meter_id, ((number_of_miutes*60) + utc_now.second))
    query_result = influxdb.query(query)
    if query_result:
        query_result = query_result[0]
        return round(query_result['points'][0][1], 2)
    return 0

def get_current_demand():
    utc_now = datetime.utcfromtimestamp(time.time()) # current request time
    # round to nearest 15-min interval, and calculate minutes difference
    number_of_miutes = utc_now.minute % 15
    customer_tz = timezone(current_user.timezone)
    result = dict()
    #utc_now.strftime('%Y-%m-%d %H:%M:%S')
    # (number_of_miutes * 60), to get the seconds precision
    consumption = 0.0
    for meter in current_user.facility:
        consumption += _get_power_avg(meter.id, number_of_miutes, utc_now)
    generation = 0.0
    for meter in current_user.solar:    
        generation += _get_power_avg(meter.id, number_of_miutes, utc_now)

    result['current_demand'] = consumption - generation
    result['time'] = customer_tz.fromutc(utc_now).strftime('%Y-%m-%d %H:%M:%S')
    return result

def get_max_peak_demand():
    utc_now = datetime.utcfromtimestamp(time.time()) # current request time
    tariff_data = utils.get_tariff_details()
    if tariff_data['season'] == 'Winter':
        return get_max_demand_anytime()
    customer_tz = timezone(tariff_data['timezone'])
    customer_tz_now = customer_tz.fromutc(utc_now)
    time_diff = customer_tz_now - customer_tz.localize(datetime.strptime(tariff_data['billing_period_startdate'], '%Y-%m-%d %H:%M:%S'))
    max_demands = dict()
    result = dict()
    for meter in current_user.facility:
        query = 'select max(demand) from "%s_%s_15mins_%s_onpeak" where time > now() - %ss;' % (current_user.get_id(), meter.id, tariff_data['season'], time_diff.total_seconds())
        query_result = influxdb.query(query)
        if query_result:
            query_result = query_result[0]
            max_demand = round(query_result['points'][0][1], 2)
            time_point_query = 'select time from "%s_%s_15mins_%s_onpeak" where demand>%s and demand<%s;' % (current_user.get_id(), meter.id, tariff_data['season'], max_demand-1, max_demand+1)
            time_point_query_result = influxdb.query(time_point_query)
            if time_point_query_result:
                max_demands[max_demand] = customer_tz.fromutc(datetime.utcfromtimestamp(time_point_query_result[0]['points'][0][0])).strftime('%Y-%m-%d %H:%M:%S')
    result['max_demand'] = max(max_demands.keys())
    result['time'] = max_demands[result['max_demand']]
    return result

def get_max_demand_anytime():
    utc_now = datetime.utcfromtimestamp(time.time()) # current request time
    tariff_data = utils.get_tariff_details()
    customer_tz = timezone(tariff_data['timezone'])
    customer_tz_now = customer_tz.fromutc(utc_now)
    time_diff = customer_tz_now - customer_tz.localize(datetime.strptime(tariff_data['billing_period_startdate'], '%Y-%m-%d %H:%M:%S'))
    result = dict()
    max_demands = dict()
    for meter in current_user.facility:
        query = 'select max(demand) from /^%s_%s_15mins_\.*/ where time > now() - %ss;' % (current_user.get_id(), meter.id, time_diff.total_seconds())
        query_results = influxdb.query(query)
        for query_result in query_results:
            max_demand = query_result['points'][0][1]
            time_point_query = 'select time from /^%s_%s_15mins_\.*/ where demand>%s and demand<%s;' % (current_user.get_id(), meter.id, max_demand-1, max_demand+1)
            time_point_query_result = influxdb.query(time_point_query)
            if time_point_query_result:
                max_demand_time = customer_tz.fromutc(datetime.utcfromtimestamp(time_point_query_result[0]['points'][0][0])).strftime('%Y-%m-%d %H:%M:%S')
            max_demands[max_demand] = max_demand_time
    result['max_demand'] = max(max_demands.keys())
    result['time'] = max_demands[result['max_demand']]
    return result
