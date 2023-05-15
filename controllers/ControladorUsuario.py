from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from alchemyClasses.Usuario import Usuario
from models.model_usuario import obten_usuario, registra_usuario

'''
Este controlador maneja toda la lógica de los casos de uso
que involucren sólo a los usuarios: como agregar un cliente.
'''

registra_cliente_blueprint = Blueprint('registro_cliente', __name__, url_prefix="registro-cliente")

@registra_cliente_blueprint.route('/', methods=['GET', 'POST'])
def registra_cliente():
    if request.method == 'GET':
        nombre = request.form['nombre']
        apellido_p = request.form['apellido_p']
        apellido_m = request.form['apellido_m']
        email = request.form['correo']
        fecha_nacimiento = request.form['fecha_nac']
        contrasena = request.form['contrasena']
        usu = Usuario(nombre, apellido_p, email, contrasena, fecha_nacimiento, 'Cliente', apellido_m=apellido_m)

        if obten_usuario(email) is not None:
            flash("ERROR: El correo ya está registrado en un usuario")
            return redirect(url_for('registro_cliente'))
        else:
            registra_usuario(usu)
            return redirect(url_for('index'))

