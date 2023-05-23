from flask import Blueprint, flash, redirect, g, render_template, request, session, url_for
from alchemyClasses.Usuario import Usuario
from models.model_usuario import Usuario, obtener_usuario

loginBlueprint = Blueprint('login', __name__, url_prefix='/login')

@loginBlueprint.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['correo']
        nombre = request.form['nombre']
        passwd = request.form['contrasena']
        usu = [email, nombre, passwd]
        '''
        if obtener_usuario(email):
            session.clear()
            session['user_id'] = usu.nombre
            g.user = usu.nombre
            return redirect(url_for('login.success'))
        else:
            flash("ERROR: Login failed")
            return redirect(url_for('login.login'))
        '''
        session.clear()
        session['user_id'] = usu[1]
        g.user = usu[1]
        return redirect(url_for('login.success'))

    else:
        return render_template('login.html')

@loginBlueprint.route('/success', methods=['GET'])
def success():
    if session.get('user_id'):
        return render_template("success.html")
    flash("ERROR: Cookie de sesión vacía")
    return redirect(url_for('login.login'))