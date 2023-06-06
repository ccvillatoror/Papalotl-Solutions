from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for,json
from alchemyClasses.Producto import Producto
from models.modelo_producto import obtener_producto, registrar_Producto, borra_Producto,editar_Producto

'''
Este controlador maneja toda la lógica de los casos de uso
que involucren a los productos
'''

productos_blueprint = Blueprint('producto', __name__, url_prefix="/")

@productos_blueprint.route('/productos')
def productos():
    productos = Producto.query.filter().all()
    return render_template("productos.html", productos=productos)

@productos_blueprint.route('/producto/<int:id_producto>')
def mostrar_producto(id_producto):
    producto = obtener_producto(id_producto)
    if producto is None:
        return "No existe el producto"
    return render_template('producto.html', producto=producto)

@productos_blueprint.route('/eliminarProducto/<int:id_producto>')
def eliminar_producto(id_producto):
    borra_Producto(id_producto)
    return redirect('/productos')

@productos_blueprint.route('/registrarProducto', methods=['GET', 'POST'])
def agregar_producto():
    if request.method == 'POST' or request.method == 'GET':
        nombre = request.args.get('nombre')
        des = request.args.get('descripcion')
        precio = request.args.get('precio')
        cant = request.args.get('cant_inventario')

        if nombre is None or des is None or precio is None or cant is None:
            return render_template('form_registrar_producto.html')
        
        producto = Producto(cant, nombre, des, precio)
        registrar_Producto(producto)
        return redirect('/productos')
    else:
        return render_template('form_registrar_producto.html')

@productos_blueprint.route('/editarProducto/<int:id_producto>', methods=['GET'])
def editar_producto(id_producto):
    producto = obtener_producto(id_producto)
    if request.method == 'GET':
        nombre = request.args.get('nombre')
        des = request.args.get('descripcion')
        precio = request.args.get('precio')
        cant = request.args.get('cant_inventario')

        if nombre is None or des is None or precio is None or cant is None:
            return render_template('form_editar_producto.html', producto=producto)
        editar_Producto(id_producto, nombre, des, precio, cant)
        return redirect('/productos')
    else:
        return render_template('form_editar_producto.html', producto=producto)