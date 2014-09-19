from app import app
from flask.ext.mongoengine import MongoEngine
from influxdb_factory import get_influxdb

mongodb = MongoEngine(app)
influxdb = get_influxdb()
