from flask import Blueprint, session

bp = Blueprint('session', __name__, url_prefix='/session/')


@bp.route("/set")
def set_cookies():
    session['username'] = 'harry'
    return session['username']


@bp.route('/get')
def get_cookies():
    return session['username'] + session.get('username')
