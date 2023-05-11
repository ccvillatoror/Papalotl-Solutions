from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from alchemyClasses.usuario import usuario
from models.model_usuario import usuario, obten_usuario

loginBlueprint = Blueprint('login', __name__, url_prefix='/login')

@loginBlueprint.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['correo']
        nombre = request.form['nombre']
        passwd = request.form['contrasena']
        usu = usuario(email, nombre, passwd)
        if obten_usuario(email) != None:
            session.clear()
            session['user_id'] = usu.nombre
            g.user = usu.nombre
            return redirect(url_for('login.success'))
        else:
            flash("ERROR: Login failed")
            return redirect(url_for('login.login'))
    else:
        return render_template('login.html')

@loginBlueprint.route('/success', methods=['GET'])
def success():
    if session.get('user_id') != None:
        return render_template("success.html")
    flash("ERROR: Cookie de sesión vacía")
    return redirect(url_for('login.login'))