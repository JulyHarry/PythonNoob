from flask import Blueprint, Response, request

bp = Blueprint('cookies', __name__, url_prefix='/cookies')


@bp.route("/set")
def set_cookies():
    response = Response("set cookies")
    response.set_cookie("user_id", "11007700")
    response.set_cookie("uuid", "a00000000001")
    return response


@bp.route('/get')
def get_cookies():
    user_id = request.cookies.get('user_id')
    return user_id
