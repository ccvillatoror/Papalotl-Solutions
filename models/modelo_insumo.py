from alchemyClasses.insumo import insumo
from alchemyClasses._init_ import db


def insumo(nombre):
  ans = insumo.query.filter(insumo.nombre == nombre).first()
  return ans

def consultar_insumo(fecha):
  ans = insumo.query.filter(insumo.fecha == fecha).first()
  return ans
  
