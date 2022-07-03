from flask import Blueprint, render_template, request, flash, redirect, url_for

from .common import get_db_connection

bp = Blueprint('new', __name__, url_prefix='/new')


@bp.route('/', methods=('GET', 'POST'))
def new():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('标题不能为空!')
        elif not content:
            flash('内容不能为空')
        else:
            con, cursor = get_db_connection()
            cursor.execute(
                'INSERT INTO web.content (title, content, author, createtime, modifytime) VALUES (%s, %s, %s, '
                'curtime(),curtime())',
                (title, content, 'harry'))
            con.commit()
            cursor.close()
            con.close()
            return redirect(url_for('index.index'))

    return render_template('new.html')
