from alchemyClasses.__init__ import db
from alchemyClasses.Ordena import Ordena

def obtener_ordena(id_usuario, id_pedido):
    ans = Ordena.query.filter(Ordena.id_usuario == id_usuario and Ordena.id_pedido == id_pedido).first()
    return ans