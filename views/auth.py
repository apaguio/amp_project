from flask import request, session, Blueprint
from servers import r

auth_app = Blueprint('auth', __name__)

@auth_app.route("/logout", methods=["POST"])
def logout():
    session['logged_in'] = False
    return r.success()

@auth_app.route("/login", methods=["POST"])
def login():
    credentials = request.json
    if not credentials or credentials.get('username', '') != 'test' or credentials.get('password', '') != 'test':
        error = 'Invalid username or password'
        return r.error(error)
    else:
        session['logged_in'] = True
         #TODO: Updaate user_id & user_roel from db
        return r.success({
            "session_id": session.get('_id'),
            "user_id": 2,
            "user_role": "user",
            "csrf_token": session.get('csrf_token')
        })

