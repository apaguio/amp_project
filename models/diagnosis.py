from models import influxdb
from pytz import timezone
from models.powerview import get_customer_timezone

def get_ekm_data_range(meter_id, start, end):
    """
    Gets EKM data in the given datetime range
    @parm meter_id  currently ( 10068 - consumption, 10054 - solar )
    @parm start start UTC timestamp (in seconds)
    @parm end end UTC timestamp (in seconds)
    """
    query = 'select * from "%s" where time > %ss and time < %ss' % (meter_id, start, end)
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
