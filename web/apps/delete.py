from flask import Blueprint, flash, redirect, url_for

from .common import get_db_connection, get_post

bp = Blueprint('delete', __name__, url_prefix='/delete/')


@bp.route('/<int:id>', methods=['POST', ])
def delete(id):
    post = get_post(id)
    con, cursor = get_db_connection()
    cursor.execute('DELETE FROM content WHERE contentid = %(id)s', {'id': id})
    con.commit()
    cursor.close()
    con.close()
    flash('"{}" 删除成功!'.format(post['title']))
    return redirect(url_for('index.index'))
