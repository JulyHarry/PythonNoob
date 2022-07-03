from flask import Blueprint, render_template

from .common import get_db_connection

bp = Blueprint('index', __name__, url_prefix='/')


@bp.route('/')
def index():
    con, cursor = get_db_connection()
    cursor.execute('SELECT * FROM web.content order by modifytime desc, contentid desc')
    posts = cursor.fetchall()
    cursor.close()
    con.close()
    return render_template('index.html', posts=posts)
