from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for

from alchemyClasses.Pedido import Pedido

pedidos_blueprint = Blueprint('pedidos', __name__, url_prefix="/pedidos")

@pedidos_blueprint.route('/pedidos', methods=['GET', 'POST'])
def mostrar_pedidos():
    if request.method == 'POST':
        pass
    else:
        pedidos = Pedido.query.filter().all()
        return render_template("pedidos.html", pedidos=pedidos)

@pedidos_blueprint.route('/pedido/<int:id_pedido>', methods=['GET', 'POST'])
def mostrar_pedido(id_pedido):
    if request.method == 'POST':
        return redirect(url_for("pedidos_blueprint.mostrar_pedidos"))
    else:
        pedido = Pedido.query.filter(Pedido.id_pedido == id_pedido).first()
        return render_template("pedidos.html", pedido=pedido)
