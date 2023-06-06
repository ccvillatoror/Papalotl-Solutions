from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from datetime import datetime
from alchemyClasses.Usuario import Usuario
from alchemyClasses.Pedido import Pedido
from models.model_usuario import obtener_usuario, registrar_usuario, actualizar_direccion_envio
from models.modelo_producto import obtener_producto
from models.ModeloPedido import registrar_pedido, obtener_pedido_fecha

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
        email = request.form['correo']
        fecha_nacimiento = request.form['fecha_nac']
        fecha_nacimiento = datetime.strptime(fecha_nacimiento, '%Y-%m-%d')
        contrasena = request.form['contrasena']

        usuario = Usuario(nombre, apellido_p, email, contrasena, fecha_nacimiento, 'Cliente', apellido_m=apellido_m)

        if obtener_usuario(email):
            flash("Error: El correo ya está registado en un usuario.")
            return redirect(url_for("registro_cliente"))
        else:
            registrar_usuario(usuario)
            flash("Usuario registrado con éxito.")
            return redirect(url_for("home"))
    else:
        return render_template("registro_cliente.html")


direccion_envio_blueprint = Blueprint('direccion_envio', __name__, url_prefix="/direccion-envio")
@direccion_envio_blueprint.route('/direccion-envio/<int:id_producto>', methods=['GET', 'POST'])
def direccion_envio(id_producto):
    if 'usuario' in session:
        correo = session['usuario']
        usuario = obtener_usuario(correo)
        producto = obtener_producto(id_producto)

        if request.method == 'POST':
            calle = request.form['calle']
            session['calle'] = calle
            num = request.form['num']
            cp = request.form['cp']
            colonia = request.form['colonia']
            ciudad = request.form['ciudad']
            estado = request.form['estado']

            actualizar_direccion_envio(usuario, calle, num, cp, colonia, ciudad, estado)
            flash("La dirección se ha guardado.")

            precio = producto.precio
            pedido = registrar_pedido(Pedido(precio, 1, 0))


            session['pedido'] = pedido.id_pedido
            session['cantidad'] = 1
            session['fecha_pedido'] = pedido.fecha
            session['producto'] = producto.id_producto

            return redirect(url_for("pago"))
        else:
            calle = usuario.dir_calle
            num = usuario.dir_num
            cp = usuario.dir_cp
            colonia = usuario.dir_colonia
            ciudad = usuario.dir_ciudad
            estado = usuario.dir_estado
            return render_template('direccion_envío.html', calle=calle, num=num,
                                   cp=cp, colonia=colonia, ciudad=ciudad, estado=estado)

    else:
        flash("Inicia sesión antes de comprar.")
        return redirect(url_for("login"))


