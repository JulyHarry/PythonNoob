from flask import Blueprint, render_template, request

from kits import create_user, SUCCESS_FLAG

bp = Blueprint('user', __name__, url_prefix='/')


@bp.route("/login")
def login():
    return render_template("login.html")


@bp.route("/register", methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        nickname = request.form['nickname']
        password = request.form['password']
        passwordConfirm = request.form['passwordConfirm']
        info = (email, username, nickname, password)
        res = create_user(info)
        if res == SUCCESS_FLAG:
            return "注册成功"
        else:
            return res
    else:
        return render_template('register.html')
