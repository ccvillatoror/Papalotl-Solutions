from Producto import Producto
from Cliente import Cliente
from InfoPago import InfoPago
import datetime
class Pedido:
    def __init__(self, idPedido, producto:Producto, cantidad, comprador:Cliente, total, estatus, infoPago:InfoPago):
        self.idPedido = idPedido
        self.producto = producto
        self.cantidad = cantidad
        self.comprador = comprador
        self.total = total
        self.estatus = estatus
        self.fecha = datetime.datetime.now()
        self.infoPago = infoPago