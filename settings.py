from celery.schedules import crontab
from datetime import timedelta

DEBUG = True
SECRET_KEY = 'L\x87V\x84\xc6\x82r\x7f\x91WXj\xfe\x19\xa67\xc9ik>.\x9b\x1aE'
SERVER_NAME = 'localhost:5000'
HOST = '0.0.0.0'
POST = 5000

# mongodb settings
MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
MONGODB_DB = 'cenergy_insights'

# influxdb settings
INFLUXDB_HOST = 'localhost'
INFLUXDB_PORT = 8086
INFLUXDB_DB = 'cenergy_insights'

# celery settings
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT=['json']
CELERY_IMPORTS = ['tasks',]

# celerybeat-mongo settings
CELERY_MONGODB_SCHEDULER_DB = 'cenergy_insights'
CELERY_MONGODB_SCHEDULER_COLLECTION = 'schedules'

# EKM metering scheduled tasks, interval in seconds
EKM_READING_INTERVAL = 5