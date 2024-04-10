# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, url_for, redirect

bp = Blueprint('index', __name__, url_prefix='/')


@bp.route('/')
def index():
    return render_template('index.html')


@bp.route('/post', methods={'POST'})
def test():
    return render_template('index2.html')
