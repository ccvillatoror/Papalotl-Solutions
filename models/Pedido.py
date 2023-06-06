from alchemyClasses.pedido import pedido
from alchemyClasses._init_ import db

def pedido(estatus):
  ans = pedido.query.filter (pedido.estatus == estatus).first
  retunr ans 
  

def reporte_venta(estatus):
  ans = pedido.query.filter(pedido.estatus == estatus).first
  return 
