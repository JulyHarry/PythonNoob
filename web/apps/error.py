from flask import Blueprint, abort, render_template

bp = Blueprint('error', __name__, url_prefix='/error')


@bp.route('/')
def error():
    abort(401)
    return {"error": "null"}


@bp.errorhandler(404)
def page_not_found(error):
    bp.logger.error("no pages")
    return render_template('page_not_found.html'), 404
