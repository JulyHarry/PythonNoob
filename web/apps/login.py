from flask import Blueprint, render_template, request

from .forms import LoginForm

bp = Blueprint('login', __name__, url_prefix='/login')


@bp.route('/', methods=('GET', 'POST'))
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        form = LoginForm(request.form)
        if form.validate():
            return "登陆成功"
        else:
            return "登陆失败"
