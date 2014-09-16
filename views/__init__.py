from flask import request, session
from app import app, r


@app.route("/logout", methods=["POST"])
def logout():
    session['logged_in'] = False
    return r.success()

@app.route("/login", methods=["POST"])
def login():
    credentials = request.json
    if credentials['username'] != 'test' or credentials['password'] != 'test':
        error = 'Invalid username or password'
        return r.error(error)
    else:
        session['logged_in'] = True
        # TODO: Updaate user_id & user_roel from db
        return r.success({
            "session_id": session.get('_id'),
            "user_id": 2,
            "user_role": "user",
            "csrf_token": session.get('csrf_token')
        })



