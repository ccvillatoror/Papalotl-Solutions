from flask import Flask, render_template, url_for, redirect, request, Blueprint, jsonify

from alchemyClasses.Pedido import Pedido
from alchemyClasses.Usuario import Usuario
from controllers.login import loginBlueprint
from alchemyClasses.__init__ import db
from alchemyClasses.Producto import Producto
from alchemyClasses.Conforma import Conforma
from alchemyClasses.Ordena import Ordena
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from controllers.ControladorUsuario import registro_cliente_blueprint

DATABASE_NAME = "micheladasatucasa"
DATABASE_USERNAME = "root"
DATABASE_PASSWORD = "root"
DATABASE_HOST = "localhost:3306"

app = Flask(__name__)
app.register_blueprint(registro_cliente_blueprint)
app.register_blueprint(loginBlueprint)
#app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://natalia:ati_desa15@localhost:3306/prueba"

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://'+DATABASE_USERNAME+':'+DATABASE_PASSWORD+'@'+DATABASE_HOST+'/'+DATABASE_NAME
app.config.from_mapping(
    SECRET_KEY='dev'
)

#db = SQLAlchemy()
#db.init_app(app)
def create_app():
    db.init_app(app)
    return app

create_app()

with app.app_context():
    try:
        db.session.execute(text('SELECT 1'))
        print('\n\n----------- Connection successful ! -----------')
    except Exception as e:
        print('\n\n----------- Connection failed ! ERROR : ', e)


# ---------------------------
@app.route('/editarProducto/<int:producto_id>', methods=['GET'])
def mostrar_formulario_editar_producto(producto_id):
    producto = Producto.query.get(producto_id)
    return render_template('formulario_editar.html', producto=producto)


@app.route('/editarProducto/<int:producto_id>', methods=['POST'])
def modificar_producto(producto_id):
    producto = Producto.query.get(producto_id)

    producto.nombre = request.form['nombre']
    producto.descripcion = request.form['descripcion']
    producto.precio = request.form['precio']
    db.session.commit()
    return 'Producto actualizado correctamente'


# ---------------------------
@app.route('/registrarProducto')
def mostrar_registro_producto():
    return render_template("form_registrar_producto.html")


@app.route('/reProducto', methods=['GET', 'POST'])
def registro_produto():
    if request.method == 'GET':
        nombre = request.args.get('nombre')
        des = request.args.get('descripcion')
        precio = request.args.get('precio')
        cant = request.args.get('cant_inventario')
        error = None

        producto = Producto(cant, nombre, des, precio)
        if not nombre:
            error = 'Se requiere nombre'
        elif not precio:
            error = 'Se requiere precio'
        db.session.add(producto)
        db.session.commit()
    return redirect('/productos')


# ---------------------------
@app.route('/productos')
def mostrar_productos():
    productos = db.session.execute(text('SELECT * FROM producto'))
    return render_template('productos.html', productos=productos)


# ---------------------------
@app.route('/producto/<int:idProducto>')
def mostrar_producto(idProducto):
    query = text('SELECT * FROM producto WHERE idProducto = :idProducto')
    producto = db.session.execute(query, {'idProducto':idProducto})
    producto = producto.fetchone()
    if producto is None:
        return render_template('errorProducto.html')
    return render_template('producto.html', producto=producto)


# ---------------------------
@app.route('/eliminarProducto/<int:producto_id>', methods=['GET'])
def eliminar_producto(producto_id):
    producto = Producto.query.get(producto_id)
    db.session.delete(producto)
    db.session.commit()
    return 'Producto eliminado correctamente'


@app.route('/eliminarP/')
def mostrar_productos_eliminar():
    return render_template('eliminar_productos.html')

@app.route("/")
def home():
    productos = Producto.query.filter().all()
    return render_template("casa.html", productos=productos)

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        return redirect(url_for("login.login"))
    else:
        return render_template("login.html")

@app.route("/registro-cliente", methods=["GET","POST"])
def registro_cliente():
    if request.method == "POST":
        return redirect(url_for("registro_cliente.registro_cliente"))
    else:
        return render_template("registro_cliente.html")

@app.route("/<usr>")
def user(usr):


    '''f usr is not None:
        if isinstance(usr,Pedido):
            return f"<h1>{usr.total}</h1>"
        else:
            tipo = type(usr)
            print(tipo)
            print(usr)
            return f"<h1>No es instancia de Pedido, es {tipo}</h1>"
    else:
        return f"<h1>Es Nulo    </h1>"'''

    return f"<h1>{usr}</h1>"

@app.route('/pedidos')
def mostrar_pedidos():
    pedidos = Pedido.query.filter(Pedido.estatus).all()
    return render_template('pedidos.html', pedidos=pedidos)

@app.route('/pedido/<int:id_pedido>')
def mostrar_pedido(id_pedido):
    pedido = Pedido.query.filter(Pedido.id_pedido == id_pedido).first()
    id_producto = Conforma.query.filter(Conforma.id_pedido == id_pedido).first().id_producto
    cantidad = Conforma.query.filter(Conforma.id_pedido == id_pedido).first().cantidad
    producto = Producto.query.filter(Producto.id_producto == id_producto).first()
    id_cliente = Ordena.query.filter(Ordena.id_pedido == id_pedido).first().id_usuario
    cliente = Usuario.query.filter(Usuario.id_usuario == id_cliente).first()
    return render_template('pedido.html', pedido=pedido, producto=producto, cliente=cliente, cantidad=cantidad)

if __name__ == '__main__':
     app.run(port=5000, debug=True)