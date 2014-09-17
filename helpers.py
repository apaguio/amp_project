from flask.ext.jsonpify import jsonify
from werkzeug.routing import BaseConverter


class RegexConverter(BaseConverter):
    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]


class CreateResponse(object):

    def __init__(self):
        pass

    def error(self, message, code=0, data={}):
        return jsonify({
            "status" : "error",
            "message": message,
            "data" : data,
            "code": code
        });

    def success(self, data={}, code=200):
        return jsonify({
            "status" : "success",
            "data" : data,
            "code" : code
        });

