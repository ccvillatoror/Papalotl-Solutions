from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for,json
from alchemyClasses.Ordena import Ordena
from alchemyClasses.Conforma import Conforma
from alchemyClasses.Pedido import Pedido
from models.model_usuario import obtener_usuario

comprar_producto_blueprint = Blueprint('comprar_producto', __name__, url_prefix='/comprar-producto')
@comprar_producto_blueprint.route('/', methods=['GET', 'POST'])
def comprar_producto():
    if 'usuario' in session:
        correo = session['usuario']
        usuario = obtener_usuario(correo)

        if request.method == 'POST':
            # Request.form
            cantidad = request.form['cantidad']
            total = request.form['total']
            # Obtener id_producto
            # Guardar total y cantidad
            # Crear Pedido

            session['pedido'] = Pedido(total, 1, 0)
            #return redirect(url_for("direccion_evio"))
            return session['pedido']
        else:
            return render_template('comprar_producto.html')
    else:
        flash("Inicia sesión antes de comprar.")
        return redirect(url_for("login"))


