from alchemyClasses.Conforma import Conforma
from alchemyClasses.Ordena import Ordena
from alchemyClasses.Pedido import Pedido
from alchemyClasses.Producto import Producto
from alchemyClasses.Usuario import Usuario
from alchemyClasses.__init__ import db

def obten_pedido(id_pedido):
    ans = Pedido.query.filter(Pedido.id_pedido == id_pedido).first()
    return ans

def crear_pedido(total, estatus):
    db.session.add(Pedido(total, estatus))
    db.session.commit()

def info_basica(id_pedido):
    info_pedido = {}
    pedido = Pedido.query.filter(Pedido.id_pedido == id_pedido).first()
    id_producto = Conforma.query.filter(
        Conforma.id_pedido == id_pedido).first().id_producto
    info_pedido["id_producto"] = id_producto
    info_pedido["id_pedido"] = id_pedido
    info_pedido["total"] = pedido.total
    info_pedido["fecha"] = pedido.fecha
    cantidad = Conforma.query.filter(
        Conforma.id_pedido == id_pedido).first().cantidad
    producto = Producto.query.filter(
        Producto.id_producto == id_producto).first().nombre
    info_pedido["cantidad"] = cantidad
    info_pedido["producto"] = producto
    id_cliente = Ordena.query.filter(
        Ordena.id_pedido == id_pedido).first().id_usuario
    info_pedido["id_cliente"] = id_cliente
    return info_pedido

def atender(id_pedido):
    Pedido.query.filter(Pedido.id_pedido == id_pedido).update({'estatus': 0})