from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for,json
from datetime import datetime
from alchemyClasses.Usuario import Usuario
from models.model_usuario import obtener_usuario, registrar_usuario, actualizar_direccion_envio

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

        if obtener_usuario(email):
            flash("Error: El correo ya está registrado en un usuario.")
            return redirect(url_for("registro_cliente"))
        else:
            registrar_usuario(usuario)
            flash("Usuario registrado con éxito.")
            return redirect(url_for("home"))
    else:
        return render_template("registro_cliente.html")


direccion_envio_blueprint = Blueprint('direccion_envio', __name__, url_prefix="/direccion-envio")
@direccion_envio_blueprint.route('/', methods=['GET', 'POST'])
def direccion_envio():
    if 'usuario' in session:
        correo = session['usuario']
        usuario = obtener_usuario(correo)
        if request.method == 'POST':

            calle = request.form['calle']
            num = request.form['num']
            cp = request.form['cp']
            colonia = request.form['colonia']
            ciudad = request.form['ciudad']
            estado = request.form['estado']
            dirección = [calle, num, cp, colonia, ciudad, estado]

            actualizar_direccion_envio(usuario, calle, num, cp, colonia, ciudad, estado)

            # TODO: Recuperar Dirección si hay
            # TODO: Actualizar los datos (?)
            return dirección
        else:
            calle = usuario.dir_calle
            num = usuario.dir_num
            cp = usuario.dir_cp
            colonia = usuario.dir_colonia
            ciudad = usuario.dir_ciudad
            estado = usuario.dir_estado
            return render_template('direccion_envío.html')

    else:
        flash("Inicia sesión antes de comprar.")
        return redirect(url_for("login"))


pago_blueprint = Blueprint('pago', __name__, url_prefix="/pago")
@pago_blueprint.route('/', methods=['GET', 'POST'])
def pago():
    if request.method == 'POST':
        print('POST gege')
        flash("Pago exitoso.")
        flash("La compra ha sido registrada.")
        # TODO: Crear la transacción
        return render_template('casa.html')
    else:
        print('GET jeje')
        return render_template('casa.html')
