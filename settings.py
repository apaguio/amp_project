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
INFLUXDB_HOST = 'eam.im'
INFLUXDB_PORT = 8086
INFLUXDB_DB = 'cenergy_insights'

# celery settings
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT=['json']
CELERY_IMPORTS = ["tasks",]

# twilio settings
TWILIO_ACCOUNT_SID = ''
TWILIO_AUTH_TOKEN = ''
TWILIO_NUMBER = ''

# EKM metering scheduled tasks
EKM_READING_INTERVAL = 5

CELERYBEAT_SCHEDULE = {
    'ekm.facility': {
        'task': 'tasks.ekm.collect',
        'schedule': EKM_READING_INTERVAL,
        'args': ('10054', EKM_READING_INTERVAL, 'MTAxMDoyMDIw', 'io.ekmpush.com', False)
    },
    'ekm.solar': {
        'task': 'tasks.ekm.collect',
        'schedule': EKM_READING_INTERVAL,
        'args': ('10068', EKM_READING_INTERVAL, 'MTAxMDoyMDIw', 'io.ekmpush.com', True)
    },
    'ekm.facility.15mins.aggregator': {
        'task': 'tasks.ekm.facility.15mins.aggregator',
        'schedule': crontab(minute=[0, 15, 30, 45]),
        'args': ('test', '10054', '10068')
    },
    'facility.energy.usage.aggregator': {
        'task': 'tasks.energy.1h.aggregator',
        'schedule': crontab(minute=0),
        'args': ('test', '10054')
    },
    'solar.energy.production.aggregator': {
        'task': 'tasks.energy.1h.aggregator',
        'schedule': crontab(minute=0),
        'args': ('test', '10068')
    },
    # facility resolution.aggregator series
    'ekm.facility.1m.aggregator': {
        'task': 'tasks.ekm.meter.resolution.aggregator',
        'schedule': timedelta(minutes=1),
        'args': ('10054', '1m')
    },
    'ekm.facility.5m.aggregator': {
        'task': 'tasks.ekm.meter.resolution.aggregator',
        'schedule': timedelta(minutes=5),
        'args': ('10054', '5m')
    },
    'ekm.facility.15m.aggregator': {
        'task': 'tasks.ekm.meter.resolution.aggregator',
        'schedule': timedelta(minutes=15),
        'args': ('10054', '15m')
    },
    'ekm.facility.30m.aggregator': {
        'task': 'tasks.ekm.meter.resolution.aggregator',
        'schedule': timedelta(minutes=30),
        'args': ('10054', '30m')
    },
    'ekm.facility.1h.aggregator': {
        'task': 'tasks.ekm.meter.resolution.aggregator',
        'schedule': timedelta(hours=1),
        'args': ('10054', '1h')
    },
    'ekm.facility.24h.aggregator': {
        'task': 'tasks.ekm.meter.resolution.aggregator',
        'schedule': timedelta(hours=24),
        'args': ('10054', '24h')
    },
    # solar resolution.aggregator series
    'ekm.solar.1m.aggregator': {
        'task': 'tasks.ekm.meter.resolution.aggregator',
        'schedule': timedelta(minutes=1),
        'args': ('10068', '1m')
    },
    'ekm.solar.5m.aggregator': {
        'task': 'tasks.ekm.meter.resolution.aggregator',
        'schedule': timedelta(minutes=5),
        'args': ('10068', '5m')
    },
    'ekm.solar.15m.aggregator': {
        'task': 'tasks.ekm.meter.resolution.aggregator',
        'schedule': timedelta(minutes=15),
        'args': ('10068', '15m')
    },
    'ekm.solar.30m.aggregator': {
        'task': 'tasks.ekm.meter.resolution.aggregator',
        'schedule': timedelta(minutes=30),
        'args': ('10068', '30m')
    },
    'ekm.solar.1h.aggregator': {
        'task': 'tasks.ekm.meter.resolution.aggregator',
        'schedule': timedelta(hours=1),
        'args': ('10068', '1h')
    },
    'ekm.solar.24h.aggregator': {
        'task': 'tasks.ekm.meter.resolution.aggregator',
        'schedule': timedelta(hours=24),
        'args': ('10068', '24h')
    },
    # alerts
    'one.minute.netload.avg.check': {
        'task': 'tasks.one.minute.netload.avg.check',
        'schedule': timedelta(minutes=1),
        'args': ('test', '10054', '10068')
    },
    'power.factor.check': {
        'task': 'tasks.power.factor.check',
        'schedule': timedelta(seconds=30),
        'args': ('test', '10054')
    },
    'voltage.check': {
        'task': 'tasks.voltage.check',
        'schedule': timedelta(seconds=30),
        'args': ('test', '10054')
    },
}
