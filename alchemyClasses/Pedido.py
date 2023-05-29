from alchemyClasses.__init__ import db
import datetime

class Pedido(db.Model):

    id_pedido = db.Column('idPedido', db.Integer, primary_key=True) # Entero de autoincremento.
    total = db.Column('total', db.Numerable(6,2), nullable=False)
    estatus = db.Column('estatus', db.Boolean)
    fecha = db.Column('fecha', db.DateTime)

    def __init__(self, total, estatus,fecha):
        self.total = total
        self.estatus = estatus
        self.fecha = datetime.datetime.now()
        
    def reporte_pedido(self, total, estatus, fecha):
        self.total = total
        self.estatus = estatus
        self.fecha = fecha
