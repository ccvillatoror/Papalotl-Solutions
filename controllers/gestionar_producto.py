from flask import flash, request
from alchemyClasses import db
from alchemyClasses.Producto import Producto


def registra_producto():
    if request.method == 'GET':
        nombre = request.args.get('nombre')
        des = request.args.get('descripcion')
        precio = request.args.get('precio')
        cant = request.form['cant_inventario']
        error = None
        if not nombre:
            error = 'Se requiere nombre'
        elif not precio:
            error = 'Se requiere precio'

        if error is None:
            try:
                db.execute(
                    "INSERT INTO producto (nombre, descripcion, precio, cant_inventario) "
                    "VALUES (?, ?, ?, ?)",
                    (0, nombre, des, precio),
                )
                db.commit()
            except db.IntegrityError:
                error = f"Producto {nombre} ya esta registrado."
        flash(error)


def actualizar_producto(producto_id):
    producto = Producto.query.get(producto_id)

    producto.nombre = request.form['nombre']
    producto.descripcion = request.form['descripcion']
    producto.precio = request.form['precio']

    db.session.commit()

    return 'Producto actualizado correctamente'

