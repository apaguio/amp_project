from models import influxdb
from pytz import timezone
from models.powerview import get_customer_timezone
from datetime import datetime

def get_ekm_data_range(meter_id, start, end, resolution=None):
    """
    Gets EKM data in the given datetime range
    @parm meter_id  currently ( 10068 - consumption, 10054 - solar )
    @parm start start UTC timestamp (in seconds)
    @parm end end UTC timestamp (in seconds)
    @parm resolution data resolution, i.e aggregation interval, same format as period, like: 1m, 5m, etc
          leave it None (default) to get 1s resolution, i.e all data available (large data sets)
    """
    if not resolution:
        query = 'select * from "%s" where time > %ss and time < %ss;' % (meter_id, start, end)
    else:
        query = '''select mean(P) as P, mean(L1_PF) as L1_PF, mean(L1_V) as L1_V
                   from "%s" where time > %ss and time < %ss group by time(%s);''' % (meter_id, start, end, resolution)
    query_result = influxdb.query(query)
    result = list()
    if query_result:
        query_result = query_result[0]
        customer_tz = timezone(get_customer_timezone(customer_name='test')) # TODO replace with current customer_id
        for point in query_result['points']:
            point_dict = dict()
            for i, value in enumerate(point):
                if query_result['columns'][i] == 'time':
                    point_dict[query_result['columns'][i]] = customer_tz.fromutc(datetime.utcfromtimestamp(value)).strftime('%Y-%m-%d %H:%M:%S')
                else:
                    point_dict[query_result['columns'][i]] = round(value, 2)
                result.append(point_dict)
    return result
