import time
from models import db, influxdb
from pytz import timezone
from datetime import datetime
from flask_login import current_user

def get_tariff_details():
    """
    Gets the tariff Details
    """
    #TODO use customer_id instead of name
    result = dict()
    utc_now = datetime.utcfromtimestamp(time.time()) # current request time
    customer = current_user
    customer_tz = timezone(customer.timezone)
    customer_tz_now = customer_tz.fromutc(utc_now)
    if customer:
        result['timezone'] = customer.timezone
        result['rate_tariff'] = customer.read_cycle.rate_tariff
        result['read_cycle'] = customer.read_cycle.name
        for season in customer.seasons:
            if customer_tz.localize(season.start) <= customer_tz_now and customer_tz.localize(season.end) >= customer_tz_now:
                result['season'] = season.name
                result['season_startdate'] = season.start.strftime('%Y-%m-%d %H:%M:%S')
                result['season_enddate'] = season.end.strftime('%Y-%m-%d %H:%M:%S')
                for peak_period in season.peak_periods:
                    for schedule in peak_period.schedule:
                        if customer_tz_now.weekday() == schedule.day_of_week and _is_time_in_range(schedule.start, schedule.end, customer_tz_now.time().isoformat().split('.')[0]):
                            result['peak_period'] = peak_period.name
                            result['peak_period_start'] = schedule.start
                            result['peak_period_end'] = schedule.end
                            result['energy_charge'] = peak_period.energy_charge
                            result['demand_charge'] = peak_period.demand_charge
                            result['peak_demand_charge'] = peak_period.peak_demand_charge
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

def _is_time_in_range(start, end, x):
    """Return true if x is in the range [start, end]"""
    if start <= end:
        return start <= x <= end
    else:
        return start <= x or x <= end

def collect_ekm_data(query):
    query_result = influxdb.query(query)
    result = list()
    if query_result:
        query_result = query_result[0]
        customer_tz = timezone(current_user.timezone) # TODO replace with current customer_id
        for point in query_result['points']:
            point_dict = dict()
            for i, value in enumerate(point):
                if query_result['columns'][i] == 'time':
                    point_dict[query_result['columns'][i]] = customer_tz.fromutc(datetime.utcfromtimestamp(value)).strftime('%Y-%m-%d %H:%M:%S')
                else:
                    point_dict[query_result['columns'][i]] = round(value, 2)
            result.append(point_dict)
    return result

acceptableResolutions = ['1m', '5m', '15m', '30m', '1h']
def acceptableResolution(resolution):
    if resolution in acceptableResolutions:
        return resolution
    return False


def generate_demo_data():
    import demo_data
    demo_data.generate()

def from_utc(utcTime, fmt="%Y-%m-%dT%H:%M:%S.%fZ"):
    """
    Convert UTC time string to time.struct_time
    """
    # change datetime.datetime to time, return time.struct_time
    # type
    return datetime.strptime(utcTime, fmt)
