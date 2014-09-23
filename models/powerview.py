import time
from datetime import datetime
from models import db
from models import influxdb

def get_ekm_data(meter_id, period):
    """
    Gets EKM Data
    @parm meter_id  currently ( 10068 - consumption, 10054 - solar )
    @parm period    time window in appended by time letter ( s - seconds, m - minutes, h - hours, d - days)
    """
    query = 'select * from "%s" where time > now() - %s limit 1000;' % (meter_id, period)
    result = influxdb.query(query)
    if result:
        return result[0]
    return result

def generate_demo_data():
    import demo_data
    demo_data.generate()

def get_current_demand(meter_id):
    utc_now = datetime.utcfromtimestamp(time.time()) # current request time
    # round to nearest 15-min interval, and calculate minutes difference
    number_of_miutes = utc_now.minute % 15
    #utc_now.strftime('%Y-%m-%d %H:%M:%S')
    # (number_of_miutes * 60), to get the seconds precision
    query = 'select mean(P) as current_demand from "%s" group by time(%ss) limit 1;' % (meter_id, number_of_miutes*60)
    query_result = influxdb.query(query)
    result = dict()
    if query_result:
        query_result = query_result[0]
        for point in query_result['points']:
            for i, value in enumerate(point):
                result[query_result['columns'][i]] = value
    return result

def get_max_demand(meter_id):
    utc_now = datetime.utcfromtimestamp(time.time()) # current request time
    tarrif_data = get_tarrif_details(customer_name='test') # TODO replace with current customer_id
    number_of_days = (utc_now - datetime.utcfromtimestamp(tarrif_data['billing_period_startdate'])).days
    query = 'select max(demand) as max_demand from "%s_15mins_%s" group by time(%sd) limit 1;' % (meter_id, tarrif_data['peak_period'], number_of_days)
    result = dict()
    query_result = influxdb.query(query)
    if query_result:
        query_result = query_result[0]
        max_demand = query_result['points'][0][1]
        time_point_query = 'select time from "%s_15mins_%s" where demand=%s' % (meter_id, tarrif_data['peak_period'], max_demand)
        result['time'] = influxdb.query(time_point_query)[0]['points'][0][0]
        result['max_demand'] = max_demand
    return result

def _is_time_in_range(start, end, x):
    """Return true if x is in the range [start, end]"""
    if start <= end:
        return start <= x <= end
    else:
        return start <= x or x <= end

def get_tarrif_details(customer_name='test'):
    """
    Gets the Tarrif Details
    """
    #TODO use customer_id instead of name
    result = dict()
    utc_now = datetime.utcfromtimestamp(time.time()) # current request time
    customer = db.Customer.objects(name=customer_name).first()
    if customer:
        result['rate_tarrif'] = customer.read_cycle.rate_tarrif
        result['read_cycle'] = customer.read_cycle.name
        for season in customer.seasons:
            if season.start <= utc_now and season.end >= utc_now:
                result['season'] = season.name
                result['season_startdate'] = int((season.start - datetime(1970, 1, 1)).total_seconds())
                result['season_enddate'] = int((season.end - datetime(1970, 1, 1)).total_seconds())
                for peak_period in season.peak_periods:
                    if _is_time_in_range(peak_period.start, peak_period.end, utc_now.time().isoformat().split('.')[0]):
                        result['peak_period'] = peak_period.name
                        result['peak_period_start'] = peak_period.start
                        result['peak_period_end'] = peak_period.end
                        result['energy_charge'] = peak_period.energy_charge
                        result['demand_charge'] = peak_period.demand_charge
                        break
                break
        for billing_period in customer.read_cycle.billing_periods:
            if billing_period.start <= utc_now and billing_period.end >= utc_now:
                result['billing_period'] = billing_period.name
                result['billing_period_startdate'] = int((billing_period.start - datetime(1970, 1, 1)).total_seconds())
                result['billing_period_enddate'] = int((billing_period.end - datetime(1970, 1, 1)).total_seconds())
                result['number_of_days'] = billing_period.number_of_days
                break
    return result

