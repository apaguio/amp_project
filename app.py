from flask_settings import *
from gevent import monkey
from socketio.server import SocketIOServer
from flask import Flask
from helpers import CreateResponse
import redis

app = Flask(__name__)
app.config.from_object('flask_settings')
app.secret_key = "somesecretkey77"
# Building the Response instance that is used to form the json structure
redisServer = redis.Redis()
pubsub = redisServer.pubsub()
r = CreateResponse()

monkey.patch_all()
from views.performance import *
from views.powerview import *

PORT = 5000
SOCKETIOPORT = 5001

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=PORT)
    SocketIOServer(('', SOCKETIOPORT), app, resource="socket.io").serve_forever()

