from alchemyClasses.__init__ import db
from Producto import Producto
from Usuario import Usuario
from models.InfoPago import InfoPago
import datetime
class Pedido(db.Model):
    '''
    create table pedido (idPedido int not null auto_increment primary key, cantidad int not null,
                     total decimal(6,2) NOT NULL DEFAULT '9999.99', estatus boolean, fecha date);
    '''
    def __init__(self, idPedido, producto:Producto, cantidad, comprador:Usuario, total, estatus, infoPago:InfoPago):
        self.idPedido = idPedido
        self.producto = producto
        self.cantidad = cantidad
        self.comprador = comprador
        self.total = total
        self.estatus = estatus
        self.fecha = datetime.datetime.now()
        self.infoPago = infoPago