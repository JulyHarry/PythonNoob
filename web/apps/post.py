from flask import Blueprint, render_template

from web.kit import get_post

bp = Blueprint('post', __name__, subdomain='post', url_prefix='/post/')


@bp.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)
