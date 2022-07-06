from flask import Blueprint, render_template

bp = Blueprint('test', __name__, url_prefix='/test')


@bp.route('/1')
def sidebar():
    return render_template('test1.html')
