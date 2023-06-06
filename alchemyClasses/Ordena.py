from alchemyClasses.__init__ import db

class Ordena(db.Model):

    id_pedido = db.Column('id_pedido', db.Integer, primary_key=True)
    id_usuario = db.Column('id_usuario', db.Integer, nullable=False)

    def __init__(self, id_pedido, id_usuario):
        self.id_pedido = id_pedido
        self.id_usuario = id_usuario