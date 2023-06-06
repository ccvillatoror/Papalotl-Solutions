from alchemyClasses.__init__ import db
from alchemyClasses.Conforma import Conforma

def obtener_conforma(id_pedido, id_producto):
    ans = Conforma.query.filter(Conforma.id_pedido == id_pedido and Conforma.id_producto == id_producto).first()
    return ans