from flask import Blueprint, request, flash, redirect, url_for, render_template

from web.kit import get_post, get_db_connection

bp = Blueprint('edit', __name__, subdomain='edit', url_prefix='/editing/')


@bp.route("/<int:id>", methods=('GET', 'POST'))
def edit(id: int):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            con, cursor = get_db_connection()
            cursor.execute('UPDATE content SET title = %s, content = %s, modifytime = curtime() WHERE contentid = %s',
                           (title, content, id))
            con.commit()
            cursor.close()
            con.close()
            return redirect(url_for('index.index'))

    return render_template('edit.html', post=post)
