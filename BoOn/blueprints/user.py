import hashlib

from flask import Blueprint, render_template, request, redirect, url_for, flash, session

from BoOn.kits import create_user, SUCCESS_FLAG, RegisterForm, email_login, username_login, exist_account

bp = Blueprint('user', __name__, url_prefix='/')


@bp.route("/login", methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        info = {'account': request.form['account'],
                'email': request.form['account'],
                'password': hashlib.md5(request.form['password'].encode('utf-8')).hexdigest()}
        if exist_account(info):
            if email_login(info) or username_login(info):
                session['account'] = info['account']
                return redirect(url_for('qa.index'))
            else:
                flash('密码不正确！')
                return render_template("login.html")
        else:
            flash('该用户名或邮箱未注册，请注册后重试！')
            return render_template("login.html")
    else:
        return render_template("login.html")


@bp.route("/register", methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        form = RegisterForm(request.form)
        if not form.validate():
            flash(form.errors)
            return redirect(url_for('user.register'))

        # email = request.form['email']
        # email = request.form.get['email']
        email = form.email.data
        username = form.username.data
        nickname = form.nickname.data
        password = form.password.data
        # passwordConfirm = form.passwordConfirm.data
        x = hashlib.md5(str(password).encode('utf-8')).hexdigest()
        info = (email, username, nickname, hashlib.md5(password.encode('utf-8')).hexdigest())
        res = create_user(info)
        if res == SUCCESS_FLAG:
            flash("注册成功，请重新登录！")
            return redirect(url_for('user.login'))
        else:
            flash(res)
            return redirect(url_for('user.register'))
    else:
        return render_template('register.html')


@bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('qa.index'))
