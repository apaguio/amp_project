from models import db, influxdb
from pytz import timezone
from datetime import datetime
from flask_login import current_user

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

def generate_demo_data():
    import demo_data
    demo_data.generate()