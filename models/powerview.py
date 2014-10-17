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
    if not resolution or resolution == '1s':
        query = 'select * from "%s" where time > now() - %s;' % (meter_id, period)
    else:
        query = '''select mean(P) as P, mean(L1_PF) as L1_PF, mean(L1_V) as L1_V
                   from "%s" where time > now() - %s group by time(%s);''' % (meter_id, period, resolution)
    return utils.collect_ekm_data(query)

def get_current_demand(meter_id, solar_meter_id):
    utc_now = datetime.utcfromtimestamp(time.time()) # current request time
    # round to nearest 15-min interval, and calculate minutes difference
    number_of_miutes = utc_now.minute % 15
    customer_tz = timezone(current_user.timezone)
    #utc_now.strftime('%Y-%m-%d %H:%M:%S')
    # (number_of_miutes * 60), to get the seconds precision
    facility_query = 'select mean(P) as current_demand from "%s" where time > now() - %ss;' % (meter_id, ((number_of_miutes*60) + utc_now.second))
    facility_query_result = influxdb.query(facility_query)
    result = dict()
    if facility_query_result:
        facility_query_result = facility_query_result[0]
        current_demand = round(facility_query_result['points'][0][1], 2)
        result['current_demand'] = current_demand
        result['time'] = customer_tz.fromutc(utc_now).strftime('%Y-%m-%d %H:%M:%S')
        solar_query = 'select mean(P) as solar_power from "%s" where time > now() - %ss;' % (solar_meter_id, ((number_of_miutes*60) + utc_now.second))
        solar_query_result = influxdb.query(solar_query)
        if solar_query_result:
            solar_query_result = solar_query_result[0]
            net_load = current_demand - round(solar_query_result['points'][0][1], 2)
            result['current_demand'] = net_load
    return result

def get_max_demand(meter_id):
    utc_now = datetime.utcfromtimestamp(time.time()) # current request time
    tariff_data = utils.get_tariff_details()
    customer_tz = timezone(tariff_data['timezone'])
    customer_tz_now = customer_tz.fromutc(utc_now)
    time_diff = customer_tz_now - customer_tz.localize(datetime.strptime(tariff_data['billing_period_startdate'], '%Y-%m-%d %H:%M:%S'))
    query = 'select max(demand) as max_demand from "%s_15mins_%s_%s" where time > now() - %ss;' % (meter_id, tariff_data['season'], tariff_data['peak_period'], time_diff.total_seconds())
    result = dict()
    query_result = influxdb.query(query)
    if query_result:
        query_result = query_result[0]
        max_demand = query_result['points'][0][1]
        time_point_query = 'select time from "%s_15mins_%s_%s" where demand>%s and demand<%s;' % (meter_id, tariff_data['season'], tariff_data['peak_period'], max_demand-1, max_demand+1)
        time_point_query_result = influxdb.query(time_point_query)
        if time_point_query_result:
            result['time'] = customer_tz.fromutc(datetime.utcfromtimestamp(time_point_query_result[0]['points'][0][0])).strftime('%Y-%m-%d %H:%M:%S')
        result['max_demand'] = max_demand
    return result