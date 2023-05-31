from alchemyClasses.Producto import Producto
from alchemyClasses.__init__ import db

def obtener_producto(idProducto):
    ans = Producto.query.filter(Producto.idProducto == idProducto).first()
    return ans

def registrar_Producto(nuevo_Producto):
    db.session.add(nuevo_Producto)
    db.session.commit()
    ans = Producto.query.filter(Producto.idProducto == nuevo_Producto.idProducto).first()
    return ans

def borra_Producto(idProducto):
    producto = Producto.query.get(idProducto)
    db.session.delete(producto)
    db.session.commit()
    return True

def editar_Producto(idProducto, nombre, descripcion, precio, cant_inventario):
    producto = Producto.query.get(idProducto)
    if producto is None or nombre=="" or precio is None or cant_inventario is None:
        return False
    producto.nombre = nombre
    producto.descripcion = descripcion
    producto.precio = precio
    producto.cant_inventario = cant_inventario
    db.session.commit()
    return True