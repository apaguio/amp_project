from gevent import monkey
from socketio.server import SocketIOServer
from flask import Flask, request
from celery import Celery

app = Flask(__name__)
app.config.from_object('settings')

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

@app.errorhandler(404)
def page_not_found(error):
    return 'This route does not exist {}'.format(request.url), 404

# Preventing circular imports
def register_views(app):
    from models import mongodb
    mongodb.init_app(app)
    from views.performance import performance_app
    from views.powerview import powerview_app
    from views.historical import historical_app
    from views.auth import auth_app
    app.register_blueprint(performance_app)
    app.register_blueprint(powerview_app)
    app.register_blueprint(historical_app)
    app.register_blueprint(auth_app)


register_views(app)

SOCKETIOPORT = 5001

if __name__ == "__main__":
    app.run()
    SocketIOServer(('', SOCKETIOPORT), app, resource="socket.io").serve_forever()
