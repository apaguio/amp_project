from influxdb_factory import get_influxdb
from flask.ext.mongoengine import MongoEngine

mongodb = MongoEngine()
influxdb = get_influxdb()
