from alchemyClasses.__init__ import db

class Ordena(db.Model):
    id_usuario = db.Column('id_usuario', db.Integer, db.ForeignKey('Usuario.idUsuario'), primary_key=True, nullable=False)  # Entero de autoincremento.
    id_pedido = db.Column('id_pedido', db.Integer, db.ForeignKey('Pedido.idPedido'), primary_key=True, nullable=False)

    def __init__(self, id_usuario, id_pedido):
        self.id_usuario = id_usuario
        self.id_pedido = id_pedido