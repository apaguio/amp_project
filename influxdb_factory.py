from influxdb.client import InfluxDBClient
from settings import INFLUXDB_HOST, INFLUXDB_PORT, INFLUXDB_DB

def get_influxdb():
    client = InfluxDBClient(host=INFLUXDB_HOST, port=INFLUXDB_PORT)
    if INFLUXDB_DB not in [db['name'] for db in client.get_database_list()]:
        client.create_database(INFLUXDB_DB)
    client.switch_db(INFLUXDB_DB)
    return client
