from celery.schedules import crontab
from datetime import timedelta
from meter_settings import SOLAR_METER_ID, CONSUMPTION_METER_ID

DEBUG = True
SECRET_KEY = 'L\x87V\x84\xc6\x82r\x7f\x91WXj\xfe\x19\xa67\xc9ik>.\x9b\x1aE'
#SERVER_NAME = 'localhost:5000'
HOST = '0.0.0.0'
POST = 5000

# mongodb settings
MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
MONGODB_DB = 'cenergy_insights'

# influxdb settings
INFLUXDB_HOST = 'cenergyamp.com'
#INFLUXDB_HOST = 'localhost'
INFLUXDB_PORT = 8086
INFLUXDB_DB = 'cenergy_insights'

# celery settings
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT=['json']
CELERY_IMPORTS = ["tasks",]

# twilio settings
TWILIO_ACCOUNT_SID = 'ACf04a9654ef7dfe275e97c6a903760840'
TWILIO_AUTH_TOKEN = 'aa39b45c1d2a5a1b685ab09e26c14fb5'
TWILIO_NUMBER = '+16502854611'

# EKM metering scheduled tasks
EKM_READING_INTERVAL = 5

CELERYBEAT_SCHEDULE = {

    #'accuenergy.test': {
    #    'task': 'tasks.accuenergy.collect',
    #    'schedule': 1,
    #    'args': ()
    #},

    #'ekm.facility': {
    #    'task': 'tasks.ekm.collect',
    #    'schedule': EKM_READING_INTERVAL,
    #    'args': (CONSUMPTION_METER_ID, EKM_READING_INTERVAL, 'MTAxMDoyMDIw', 'io.ekmpush.com', False)
    #},
    #'ekm.solar': {
    #    'task': 'tasks.ekm.collect',
    #    'schedule': EKM_READING_INTERVAL,
    #    'args': (CONSUMPTION_METER_ID, EKM_READING_INTERVAL, 'MTAxMDoyMDIw', 'io.ekmpush.com', True)
    #},
    'ekm.facility.15mins.aggregator': {
        'task': 'tasks.ekm.facility.15mins.aggregator',
        'schedule': crontab(minute=[0, 15, 30, 45]),
        'args': ('test', SOLAR_METER_ID, CONSUMPTION_METER_ID)
    },
    'facility.energy.usage.aggregator': {
        'task': 'tasks.energy.1h.aggregator',
        'schedule': crontab(minute=0),
        'args': ('test', SOLAR_METER_ID)
    },
    'solar.energy.production.aggregator': {
        'task': 'tasks.energy.1h.aggregator',
        'schedule': crontab(minute=0),
        'args': ('test', CONSUMPTION_METER_ID)
    },
    # facility resolution.aggregator series
    'ekm.facility.1m.aggregator': {
        'task': 'tasks.ekm.meter.resolution.aggregator',
        'schedule': timedelta(minutes=1),
        'args': (SOLAR_METER_ID, '1m')
    },
    'ekm.facility.5m.aggregator': {
        'task': 'tasks.ekm.meter.resolution.aggregator',
        'schedule': timedelta(minutes=5),
        'args': (SOLAR_METER_ID, '5m')
    },
    'ekm.facility.15m.aggregator': {
        'task': 'tasks.ekm.meter.resolution.aggregator',
        'schedule': timedelta(minutes=15),
        'args': (SOLAR_METER_ID, '15m')
    },
    'ekm.facility.30m.aggregator': {
        'task': 'tasks.ekm.meter.resolution.aggregator',
        'schedule': timedelta(minutes=30),
        'args': (SOLAR_METER_ID, '30m')
    },
    'ekm.facility.1h.aggregator': {
        'task': 'tasks.ekm.meter.resolution.aggregator',
        'schedule': timedelta(hours=1),
        'args': (SOLAR_METER_ID, '1h')
    },
    'ekm.facility.24h.aggregator': {
        'task': 'tasks.ekm.meter.resolution.aggregator',
        'schedule': timedelta(hours=24),
        'args': (SOLAR_METER_ID, '24h')
    },
    # solar resolution.aggregator series
    'ekm.solar.1m.aggregator': {
        'task': 'tasks.ekm.meter.resolution.aggregator',
        'schedule': timedelta(minutes=1),
        'args': (CONSUMPTION_METER_ID, '1m')
    },
    'ekm.solar.5m.aggregator': {
        'task': 'tasks.ekm.meter.resolution.aggregator',
        'schedule': timedelta(minutes=5),
        'args': (CONSUMPTION_METER_ID, '5m')
    },
    'ekm.solar.15m.aggregator': {
        'task': 'tasks.ekm.meter.resolution.aggregator',
        'schedule': timedelta(minutes=15),
        'args': (CONSUMPTION_METER_ID, '15m')
    },
    'ekm.solar.30m.aggregator': {
        'task': 'tasks.ekm.meter.resolution.aggregator',
        'schedule': timedelta(minutes=30),
        'args': (CONSUMPTION_METER_ID, '30m')
    },
    'ekm.solar.1h.aggregator': {
        'task': 'tasks.ekm.meter.resolution.aggregator',
        'schedule': timedelta(hours=1),
        'args': (CONSUMPTION_METER_ID, '1h')
    },
    'ekm.solar.24h.aggregator': {
        'task': 'tasks.ekm.meter.resolution.aggregator',
        'schedule': timedelta(hours=24),
        'args': (CONSUMPTION_METER_ID, '24h')
    },
    # alerts
    'one.minute.netload.avg.check': {
        'task': 'tasks.one.minute.netload.avg.check',
        'schedule': timedelta(minutes=1),
        'args': ('test', SOLAR_METER_ID, CONSUMPTION_METER_ID)
    },
    'power.factor.check': {
        'task': 'tasks.power.factor.check',
        'schedule': timedelta(seconds=30),
        'args': ('test', SOLAR_METER_ID)
    },
    'voltage.check': {
        'task': 'tasks.voltage.check',
        'schedule': timedelta(seconds=30),
        'args': ('test', SOLAR_METER_ID)
    },
}
