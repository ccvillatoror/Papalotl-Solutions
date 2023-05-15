from alchemyClasses.Pedido import Pedido

def obten_pedido(id_pedido):
    ans = Pedido.query.filter(Pedido.id_pedido == id_pedido).first()
    return ans

def atender(id_pedido):
    Pedido.query.filter(Pedido.id_pedido == id_pedido).update({'estatus': 0})