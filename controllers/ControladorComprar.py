from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for,json
from alchemyClasses.Ordena import Ordena
from alchemyClasses.Conforma import Conforma
from alchemyClasses.Pedido import Pedido
from alchemyClasses.Producto import Producto
from models.model_usuario import obtener_usuario
from models.modelo_producto import obtener_producto
from models.model_conforma import registrar_conforma
from models.model_ordena import registrar_ordena
from models.ModeloPedido import registrar_pedido


comprar_producto_blueprint = Blueprint('comprar_producto', __name__, url_prefix='/comprar-producto')
@comprar_producto_blueprint.route('/comprar-producto/<int:idProducto>', methods=['GET', 'POST'])
def comprar_producto(idProducto):
    if 'usuario' in session:
        correo = session['usuario']
        usuario = obtener_usuario(correo)
        producto = obtener_producto(idProducto)
        inventario = [i+1 for i in range(producto.cant_inventario)]

        if request.method == 'POST':
            # Request.form
            precio = producto.precio
            cantidad = request.form['cantidad']
            total = cantidad * precio
            # Obtener id_producto
            # Guardar total y cantidad
            # Crear Pedido

            session['pedido'] = Pedido(total, 1, 0)
            session['cantidad'] = cantidad
            session['fecha_pedido'] = session['pedido'].fecha
            session['producto'] = producto
            print(session['pedido'])

            return redirect(url_for("direccion-envio"))
        else:
            return render_template('comprar_producto.html', producto=producto, inventario=inventario)
    else:
        flash("Inicia sesión antes de comprar.")
        return redirect(url_for("login"))

pago_blueprint = Blueprint('pago', __name__, url_prefix="/pago")
@pago_blueprint.route('/', methods=['GET', 'POST'])
def pago():
    if 'pedido' in session and 'usuario' in session:
        usuario = obtener_usuario(session['usuario'])
        pedido = session['pedido']
        producto = session['producto']
        cantidad = session['cantidad']
        if request.method == 'POST':
            compra = [Conforma(pedido.id_pedido, producto.idProducto, cantidad),
                      Ordena(usuario.id_usuario, pedido.id_pedido)]
            registrar_conforma(compra[0])
            registrar_ordena(compra[1])
            registrar_pedido(pedido)


            flash("Pago exitoso.")
            flash("La compra ha sido registrada.")
            return redirect(url_for('home'))
        else:
            return render_template('pago.html')
    else:
        flash("No hay ningún artículo seleccionado.")

