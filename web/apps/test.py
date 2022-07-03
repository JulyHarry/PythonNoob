from flask import Blueprint, request, url_for, redirect

bp = Blueprint('test', __name__, url_prefix='/test')


@bp.route('/test<int:id>')
def blog_int(id: int):
    return {'num': str(id)}


@bp.route('/test<string:id>')
def blog_str(id: str):
    return {'message': id}


@bp.route('/test<float:id>')
def blog_float(id: float):
    return {'float': str(id)}


@bp.route('/test<path:id>')
def blog_path(id: str):
    return {'path': str(id)}


@bp.route('/test')
def blog_get():
    a = request.args.get('id')
    return {"get(blog's id)": str(a)}


@bp.route('/test', methods=['POST'])
def post_blog_id():
    id = request.form.get('id')
    return {"post_blog_id": id}


@bp.route('/red/')
def red():
    return redirect(url_for('error.error'), code=301)
