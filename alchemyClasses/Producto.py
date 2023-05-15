from alchemyClasses.__init__ import db


class Producto(db.Model):
    id_producto = db.Column('idProducto', db.Integer, primary_key=True)  # Entero de autoincremento.
    nombre = db.Column('nombre', db.String(20))
    descripcion = db.Column('descripcion', db.String(250))
    precio = db.Column('precio', db.Numeric(6, 2), nullable=False)
    cant_inventario = db.Column('cantidadInventario', db.Integer, nullable=False)

    def __init__(self, cantidad, nombre=None, descripcion=None, precio=9999.99):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.cant_inventario = cantidad
