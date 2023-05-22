class Ventas
  def _init_(self,precio, cantidad , venta):
    self.precio = precio
    self.cantidad = cantidad
    self.venta = venta
    
  def reporte(self, registro_venta):
    self.venta = registro_venta
