from models import db, influxdb
from pytz import timezone
from datetime import datetime


def collect_ekm_data(query):
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

def get_customer_timezone(customer_name='test'):
    customer = db.Customer.objects(name=customer_name).first()
    if customer:
        return customer.timezone

def generate_demo_data():
    import demo_data
    demo_data.generate()

