import time
from datetime import datetime
from models import db
from models import influxdb
from pytz import timezone

def get_ekm_data(meter_id, period):
    """
    Gets EKM Data
    @parm meter_id  currently ( 10068 - consumption, 10054 - solar )
    @parm period    time window in appended by time letter ( s - seconds, m - minutes, h - hours, d - days)
    """
    query = 'select * from "%s" where time > now() - %s limit 1000;' % (meter_id, period)
    query_result = influxdb.query(query)
    result = list()
    if query_result:
        query_result = query_result[0]
        customer_tz = timezone(get_customer_timezone(customer_name='test')) # TODO replace with current customer_id
        for point in query_result['points']:
            point_dict = dict()
            for i, value in enumerate(point):
                point_dict[query_result['columns'][i]] = value
                result.append(point_dict)
        for point_dict in result:
            point_dict['time'] = customer_tz.fromutc(datetime.utcfromtimestamp(point_dict['time'])).strftime('%Y-%m-%d %H:%M:%S')
    return result

def generate_demo_data():
    import demo_data
    demo_data.generate()

def get_current_demand(meter_id, solar_meter_id):
    utc_now = datetime.utcfromtimestamp(time.time()) # current request time
    # round to nearest 15-min interval, and calculate minutes difference
    number_of_miutes = utc_now.minute % 15
    customer_tz = timezone(get_customer_timezone(customer_name='test')) # TODO replace with current customer_id
    #utc_now.strftime('%Y-%m-%d %H:%M:%S')
    # (number_of_miutes * 60), to get the seconds precision
    facility_query = 'select mean(P) as current_demand from "%s" group by time(%ss) limit 1;' % (meter_id, number_of_miutes*60)
    facility_query_result = influxdb.query(facility_query)
    result = dict()
    if facility_query_result:
        facility_query_result = facility_query_result[0]
        current_demand = round(facility_query_result['points'][0][1], 2)
        result['current_demand'] = current_demand
        result['time'] = customer_tz.fromutc(datetime.utcfromtimestamp(facility_query_result['points'][0][0])).strftime('%Y-%m-%d %H:%M:%S')
        solar_query = 'select mean(P) as solar_power from "%s" group by time(%ss) limit 1;' % (solar_meter_id, number_of_miutes*60)
        solar_query_result = influxdb.query(solar_query)
        if solar_query_result:
            solar_query_result = solar_query_result[0]
            net_load = current_demand - round(solar_query_result['points'][0][1], 2)
            result['current_demand'] = net_load
    return result

def get_max_demand(meter_id):
    utc_now = datetime.utcfromtimestamp(time.time()) # current request time
    tarrif_data = get_tarrif_details(customer_name='test') # TODO replace with current customer_id
    customer_tz = timezone(tarrif_data['timezone'])
    customer_tz_now = customer_tz.fromutc(utc_now)
    time_diff = customer_tz_now - datetime.strptime(tarrif_data['billing_period_startdate'], '%Y-%m-%d %H:%M:%S')
    number_of_hours = (time_diff.days * 24) + (time_diff.hours) # mroe accuracy when calculating  max demand
    query = 'select max(demand) as max_demand from "%s_15mins_%s" group by time(%sh) limit 1;' % (meter_id, tarrif_data['peak_period'], number_of_hours)
    result = dict()
    query_result = influxdb.query(query)
    if query_result:
        query_result = query_result[0]
        max_demand = query_result['points'][0][1]
        time_point_query = 'select time from "%s_15mins_%s" where demand=%s' % (meter_id, tarrif_data['peak_period'], max_demand)
        result['time'] = customer_tz.fromutc(datetime.utcfromtimestamp(influxdb.query(time_point_query)[0]['points'][0][0])).strftime('%Y-%m-%d %H:%M:%S')
        result['max_demand'] = max_demand
    return result

def _is_time_in_range(start, end, x):
    """Return true if x is in the range [start, end]"""
    if start <= end:
        return start <= x <= end
    else:
        return start <= x or x <= end

def get_customer_timezone(customer_name='test'):
    customer = db.Customer.objects(name=customer_name).first()
    if customer:
        return customer.timezone

def get_tarrif_details(customer_name='test'):
    """
    Gets the Tarrif Details
    """
    #TODO use customer_id instead of name
    result = dict()
    utc_now = datetime.utcfromtimestamp(time.time()) # current request time
    customer = db.Customer.objects(name=customer_name).first()
    customer_tz = timezone(customer.timezone)
    customer_tz_now = customer_tz.fromutc(utc_now)
    if customer:
        result['timezone'] = customer.timezone
        result['rate_tarrif'] = customer.read_cycle.rate_tarrif
        result['read_cycle'] = customer.read_cycle.name
        for season in customer.seasons:
            if customer_tz.localize(season.start) <= customer_tz_now and customer_tz.localize(season.end) >= customer_tz_now:
                result['season'] = season.name
                result['season_startdate'] = season.start.strftime('%Y-%m-%d %H:%M:%S')
                result['season_enddate'] = season.end.strftime('%Y-%m-%d %H:%M:%S')
                for peak_period in season.peak_periods:
                    if _is_time_in_range(peak_period.start, peak_period.end, customer_tz_now.time().isoformat().split('.')[0]):
                        result['peak_period'] = peak_period.name
                        result['peak_period_start'] = peak_period.start
                        result['peak_period_end'] = peak_period.end
                        result['energy_charge'] = peak_period.energy_charge
                        result['demand_charge'] = peak_period.demand_charge
                        break
                break
        for billing_period in customer.read_cycle.billing_periods:
            if customer_tz.localize(billing_period.start) <= customer_tz_now and customer_tz.localize(billing_period.end) >= customer_tz_now:
                result['billing_period'] = billing_period.name
                result['billing_period_startdate'] = billing_period.start.strftime('%Y-%m-%d %H:%M:%S')
                result['billing_period_enddate'] = billing_period.end.strftime('%Y-%m-%d %H:%M:%S')
                result['number_of_days'] = billing_period.number_of_days
                break
    return result

