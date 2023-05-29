class Ventas:
  def _init_(self,total, estatus , fecha):
    self.precio = total
    self.cantidad = estatus
    self.venta = fecha
    
  def reporte(self, registro_venta):
    self.venta = registro_venta
