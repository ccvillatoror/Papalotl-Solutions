from alchemyClasses.__init__ import db

class Conforma(db.Model):
    id_pedido = db.Column('id_pedido', db.Integer, primary_key=True, nullable=False)
    id_producto = db.Column('id_producto', db.Integer, nullable=False)
    cantidad = db.Column('cantidad', db.Integer, nullable=False)

    def __init__(self, id_pedido, id_producto, cantidad):
        self.id_pedido = id_pedido
        self.id_producto = id_producto
        self.cantidad = cantidad