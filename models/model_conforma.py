from alchemyClasses.__init__ import db
from alchemyClasses.Conforma import Conforma

def obtener_conforma(id_pedido, id_producto):
    ans = Conforma.query.filter(Conforma.id_pedido == id_pedido, Conforma.id_producto == id_producto).first()
    return ans

def registrar_conforma(nuevo_conforma):
    db.session.add(nuevo_conforma)
    db.session.commit()
    ans = Conforma.query.filter(Conforma.id_pedido == nuevo_conforma.id_pedido,
                                Conforma.id_producto == nuevo_conforma.id_producto).first()
    return ans