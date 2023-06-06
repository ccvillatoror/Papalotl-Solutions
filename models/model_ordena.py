from alchemyClasses.__init__ import db
from alchemyClasses.Ordena import Ordena

def obtener_ordena(id_usuario, id_pedido):
    ans = Ordena.query.filter(Ordena.id_usuario == id_usuario, Ordena.id_pedido == id_pedido).first()
    return ans

def registrar_ordena(nuevo_ordena):
    db.session.add(nuevo_ordena)
    db.session.commit()
    ans = Ordena.query.filter(Ordena.id_pedido == nuevo_ordena.id_pedido,
                                Ordena.id_usuario == nuevo_ordena.id_usuario).first()
    return ans