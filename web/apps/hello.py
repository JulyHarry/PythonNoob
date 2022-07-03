from flask import Blueprint, render_template

bp = Blueprint('hello', __name__, url_prefix='/hello')


@bp.route("/")
@bp.route("/<string:name>")
def hello(name=None):
    return render_template('hello.html', data=name, l=list)
