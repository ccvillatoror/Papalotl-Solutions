from alchemyClasses._init_import db

class insumo(db.Model):
  id_insumo = db.Column('idInsumo', db.Integer, primary_key = True) #int auto_increment.
  nombre = db.Column('nombre', db.String(25), nullable = True)
  cantidad = db.Column('cantidad', db.Integer, nullable = False)
  fecha = db.Column('fecha', db.DateTime, nullable = False)
  
  
  def _init_(self,nombre, cantidad, fecha):
    self.nombre = nombre
    self.cantidad = cantidad
    self.fecha = fecha
    
  def itinerario_insumo(self,nombre,cantidad,fecha):
    self.nombre = nombre
    self.cantidad = cantidad
    self.fecha = fecha
