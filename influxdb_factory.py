from influxdb.client import InfluxDBClient

def get_influxdb(db_name='cenergy_insights'):
    client = InfluxDBClient()
    if db_name not in [db['name'] for db in client.get_database_list()]:
        client.create_database(db_name)
    client.switch_db(db_name)
    return client
