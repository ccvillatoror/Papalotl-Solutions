from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for

from alchemyClasses.Pedido import Pedido
from alchemyClasses.Usuario import Usuario
from models.ModeloPedido import info_basica, atender

pedidos_blueprint = Blueprint('pedidos', __name__, url_prefix="/pedidos")

@pedidos_blueprint.route('/', methods=['GET'])
def mostrar_pedidos():
    pedidos = Pedido.query.filter(Pedido.estatus).all()
    get_id = lambda x: x.id_pedido
    id_pedidos = list(map(get_id, pedidos))
    pedidos = list(map(info_basica, id_pedidos))
    pedidos = [x for x in pedidos if x is not None]
    return render_template('pedidos.html', pedidos=pedidos)

@pedidos_blueprint.route('/pedido/<int:id_pedido>', methods=['GET'])
def mostrar_pedido(id_pedido):
    pedido = info_basica(id_pedido)
    cliente = Usuario.query.filter(
        Usuario.id_usuario == pedido["id_cliente"]).first()
    return render_template('pedido.html', pedido=pedido, cliente=cliente)

@pedidos_blueprint.route('/pedido/<int:id_pedido>/exito', methods=['GET'])
def estatus_actualizado(id_pedido):
    atender(id_pedido)
    print("Aquí se actualiza el pedido:", id_pedido)
    return render_template('estatus_actualizado.html', id_pedido=id_pedido)
