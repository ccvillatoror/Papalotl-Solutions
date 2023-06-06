from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for,json
from alchemyClasses.Ordena import Ordena
from alchemyClasses.Conforma import Conforma
from alchemyClasses.Pedido import Pedido
from alchemyClasses.Producto import Producto
from models.model_usuario import obtener_usuario
from models.modelo_producto import obtener_producto

comprar_producto_blueprint = Blueprint('comprar_producto', __name__, url_prefix='/comprar-producto')
@comprar_producto_blueprint.route('/comprar_producto/<int:idProducto>', methods=['GET', 'POST'])
def comprar_producto(idProducto):
    if 'usuario' in session:
        correo = session['usuario']
        usuario = obtener_usuario(correo)
        producto = obtener_producto(idProducto)

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
            #return redirect(url_for("direccion_evio"))
            return session['pedido']
        else:
            return render_template('comprar_producto.html')
    else:
        flash("Inicia sesión antes de comprar.")
        return redirect(url_for("login"))


