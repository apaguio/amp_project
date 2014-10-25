from flask import Blueprint, request
from servers import r
from models import db
from flask_login import login_required, current_user

settings_app = Blueprint('settings', __name__)

@settings_app.route("/settings", methods=["GET"])
@login_required
def load():
    user = db.Customer.objects(id=current_user.get_id()).first()
    del user.password
    return r.success(user)

@settings_app.route("/settings", methods=["POST"])
@login_required
def update():
    data = request.json
    user = db.Customer.objects(id=current_user.get_id()).first()
    user['password'] = data.get("password", user['password'])
    user['facility_name'] = data.get("facility_name", user['facility_name'])
    user.save()
    print user['facility_name']
    return r.success(user)

