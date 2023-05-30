from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for,json
from datetime import datetime
from alchemyClasses.Usuario import Usuario
from models.model_usuario import obtener_usuario, registrar_usuario

'''
Este controlador maneja toda la lógica de los casos de uso
que involucren sólo a los usuarios: como agregar un cliente.
'''

registro_cliente_blueprint = Blueprint('registro_cliente', __name__, url_prefix="/registro-cliente")

@registro_cliente_blueprint.route('/', methods=['GET', 'POST'])
def registro_cliente():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido_p = request.form['apellido_p']
        apellido_m = request.form['apellido_m']
        correo = request.form['correo']
        fecha_nacimiento = request.form['fecha_nac']
        fecha_nacimiento = datetime.strptime(fecha_nacimiento, '%Y-%m-%d')
        contrasena = request.form['contrasena']

        usuario = Usuario(nombre, apellido_p, correo, contrasena, fecha_nacimiento, 'Cliente', apellido_m=apellido_m)

        if obtener_usuario(correo):
            #flash("Error: El correo ya está registado en un usuario.")
            return redirect(url_for("registro_cliente"))
        else:
            registrar_usuario(usuario)
            #flash("Usuario registrado con éxito.")
            return redirect(url_for("home"))
    else:
        return render_template("registro_cliente.html")
    

login_usuario_blueprint = Blueprint('login', __name__, url_prefix="/login")
@login_usuario_blueprint.route('/', methods=['GET', 'POST'])
def login_usuario():
    print("login")
    if request.method == 'POST':
        print("post")
        correo = request.form['correo']
        contrasena = request.form['contrasena']
        usuario = obtener_usuario(correo)
        print(usuario)
        
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
