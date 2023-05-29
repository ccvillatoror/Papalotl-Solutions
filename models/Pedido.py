class Pedido:
  def _init_(self,total, estatus , fecha):
    self.total = total
    self.estatus = estatus
    self.fecha = fecha
    
  def reporte(self, registro_pedido):
    self.venta = registro_pedido
