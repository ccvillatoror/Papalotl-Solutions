import functools

from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/', methods=['GET'])
def main():
    return redirect(url_for('auth.another_index'))

@bp.route('/another-index', methods=['GET'])
def another_index():
    return render_template("another-index.html")