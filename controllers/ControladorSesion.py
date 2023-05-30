from flask import Blueprint, redirect, render_template, request, session, url_for
from models.model_usuario import obtener_usuario

login_usuario_blueprint = Blueprint('login', __name__, url_prefix="/login")
@login_usuario_blueprint.route('/', methods=['GET', 'POST'])
def login_usuario():
    if request.method == 'POST':
        correo = request.form['correo']
        contrasena = request.form['contrasena']
        usuario = obtener_usuario(correo)
        
        if usuario != None:
            if usuario.contrasena == contrasena:
                session['usuario'] = usuario.correo
                return redirect(url_for("producto.productos"))
            else:
                return "Error: Contraseña incorrecta."
        else:
            return "Error: El correo no está registrado."
    else:
        return render_template("login.html")

logout_usuario_blueprint = Blueprint('logout', __name__, url_prefix="/logout")
@logout_usuario_blueprint.route('/')
def logout_usuario():
    session.pop('usuario', None)
    return redirect(url_for("home"))
