from gevent import monkey
from socketio.server import SocketIOServer
from flask import Flask
from celery import Celery
from helpers import CreateResponse
import redis

app = Flask(__name__)
app.config.from_object('settings')
app.secret_key = "somesecretkey77"
# Building the Response instance that is used to form the json structure
redisServer = redis.Redis()
pubsub = redisServer.pubsub()
r = CreateResponse()

def make_celery(app):
    celery = Celery(app.import_name, broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)
    TaskBase = celery.Task
    class ContextTask(TaskBase):
        abstract = True
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery.Task = ContextTask
    return celery

celery = make_celery(app)

monkey.patch_all()
from views.performance import *
from views.powerview import *

PORT = 5000
SOCKETIOPORT = 5001

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=PORT)
    SocketIOServer(('', SOCKETIOPORT), app, resource="socket.io").serve_forever()