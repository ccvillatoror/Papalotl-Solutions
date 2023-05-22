from alchemyClasses.Pedido import Pedido
from alchemyClasses.__init__ import db

def obten_pedido(id_pedido):
    ans = Pedido.query.filter(Pedido.id_pedido == id_pedido).first()
    return ans

def crear_pedido(total, estatus):
    db.session.add(Pedido(total, estatus))
    db.session.commit()

def atender(id_pedido):
    Pedido.query.filter(Pedido.id_pedido == id_pedido).update({'estatus': 0})