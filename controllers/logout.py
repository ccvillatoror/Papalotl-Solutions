from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for

logoutBlueprint = Blueprint('logout', __name__, url_prefix='/logout')

@logoutBlueprint.route('/')
def root():
    return redirect(url_for('logout.logout'))

@logoutBlueprint.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login.login'))