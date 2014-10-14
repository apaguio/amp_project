from flask import request, session, Blueprint
from flask_login import login_user, logout_user
from servers import r
from models import db

auth_app = Blueprint('auth', __name__)
fake_password = 'c3nergy'

@auth_app.route("/logout", methods=["POST"])
def logout():
    logout_user()
    return r.success()

@auth_app.route("/login", methods=["POST"])
def login():
    credentials = request.json
    if not credentials:
        error = 'User name and password are missing'
        return r.error(error)
    user_name = credentials.get('username')
    customer = db.Customer.objects(name=user_name).first()
    if customer.password != credentials.get('password'):
        error = 'Invalid user name and/or password'
        return r.error(error)
    else:
        login_user(customer)
        return r.success({
            "session_id": session.get('_id'),
            "user_id": customer.uid,
            "user_role": "user",
            "csrf_token": session.get('csrf_token')
        })

