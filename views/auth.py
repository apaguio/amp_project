from flask import request, session, Blueprint
from flask_login import login_user, logout_user, login_required, current_user
from servers import r
from models import db

auth_app = Blueprint('auth', __name__)
fake_password = 'c3nergy'

@auth_app.route("/auth/logout", methods=["POST"])
def logout():
    logout_user()
    return r.success()

@auth_app.route("/auth/login", methods=["POST"])
def login():
    credentials = request.json
    if not credentials:
        error = 'User name and password are missing'
        return r.error(error)
    user_name = credentials.get('username')
    customer = db.Customer.objects(name=user_name).first()
    if customer.password != credentials.get('password'):
        error = 'Invalid user name and/or password'
        return r.error(error, 401)
    else:
        login_user(customer)
        print current_user
        return r.success({
            "name": customer["name"],
            "role": "user"
        })

@auth_app.route("/auth/load", methods=["GET"])
@login_required
def load_user():
    return r.success({
        "name": current_user["name"],
        #"role": customer["role"] or "user"
        "role": "user"
    })
