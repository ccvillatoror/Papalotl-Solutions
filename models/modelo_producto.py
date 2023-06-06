from alchemyClasses.Producto import Producto
from alchemyClasses.__init__ import db

def obtener_producto(id_producto):
    ans = Producto.query.filter(Producto.id_producto == id_producto).first()
    return ans

def registrar_Producto(nuevo_Producto):
    db.session.add(nuevo_Producto)
    db.session.commit()
    ans = Producto.query.filter(Producto.id_producto == nuevo_Producto.id_producto).first()
    return ans

def borra_Producto(id_producto):
    producto = Producto.query.get(id_producto)
    db.session.delete(producto)
    db.session.commit()
    return True

def editar_Producto(id_producto, nombre, descripcion, precio, cant_inventario):
    producto = Producto.query.get(id_producto)
    if producto is None or nombre=="" or precio is None or cant_inventario is None:
        return False
    producto.nombre = nombre
    producto.descripcion = descripcion
    producto.precio = precio
    producto.cant_inventario = cant_inventario
    db.session.commit()
    return True