from app import app
from flask.ext.pymongo import PyMongo
from influxdb_factory import get_influxdb

mongodb = PyMongo(app)
influxdb = get_influxdb()
