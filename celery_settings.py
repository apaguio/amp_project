BROKER_URL = 'redis://localhost:6379/0'
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT=['json']
CELERY_TIMEZONE = 'US/Pacific'

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
}