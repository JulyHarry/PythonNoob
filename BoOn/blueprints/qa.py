from flask import Blueprint, render_template, request, g, flash, redirect, url_for

from BoOn.kits import login_required, get_db_connection, check_primary, create_question

bp = Blueprint('qa', __name__, url_prefix='/')


@bp.route("/")
def index():
    sql = "select * from questions_info order by updatetime desc"
    con, cursor = get_db_connection()
    cursor.execute(sql)
    res = cursor.fetchall()
    print(res)
    return render_template("index.html", posts=res)


@bp.route("/publish", methods=('GET', 'POST'))
@login_required
def publish():
    if request.method == 'GET':
        return render_template("publish.html", publish={})
    else:
        publish = {'title': request.form['title'],
                   'content': request.form['content'],
                   'author': g.user_info['nickname']}
        if check_primary(publish):
            flash("已存在相同的标题，请更改新的标题后重试")
            return render_template("publish.html", publish=publish)
        create_question(publish)
        return redirect(url_for('qa.index'))


@bp.route("/question/<int:id>")
def question_detail(id: int):
    sql = "select * from questions_info where qid = %(id)s"
    info = {'id': id}
    con, cursor = get_db_connection()
    cursor.execute(sql, info)
    res = cursor.fetchone()
    return render_template("question.html", post=res)
