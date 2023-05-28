from flask import Flask, render_template, url_for, redirect, request, Blueprint, jsonify
from controllers.login import loginBlueprint
from alchemyClasses.__init__ import db
from alchemyClasses.Producto import Producto
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from controllers.ControladorUsuario import registro_cliente_blueprint



DATABASE_NAME = "micheladasatucasa"
DATABASE_USERNAME = "natalia"
DATABASE_PASSWORD = "ati_desa15"
DATABASE_HOST = "localhost:3306"

app = Flask(__name__)
app.register_blueprint(registro_cliente_blueprint)
app.register_blueprint(loginBlueprint)
#app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://natalia:ati_desa15@localhost:3306/prueba"

app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://' + DATABASE_USERNAME + ':' + DATABASE_PASSWORD + '@' + DATABASE_HOST + '/' + DATABASE_NAME
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

@app.route('/editarP/<int:idProducto>', methods=['GET'])
def modificar_producto(idProducto):
    producto = Producto.query.get(idProducto)
    if request.method == 'GET':
        nombre = request.args.get('nombre')
        des = request.args.get('descripcion')
        precio = request.args.get('precio')
        cant = request.args.get('cant_inventario')

        producto.nombre = nombre
        producto.descripcion = des
        producto.precio = precio
        producto.cant_inventario = cant
        db.session.commit()
        return redirect('/productos')
       

@app.route('/editarProducto/<int:idProducto>', methods=['GET'])
def mostrar_modificar_producto(idProducto):
    query = text('SELECT * FROM producto WHERE idProducto = :idProducto')
    producto = db.session.execute(query, {'idProducto':idProducto})
    producto = producto.fetchone()
    return render_template('form_editar_producto.html', producto=producto)


# ---------------------------
@app.route('/registrarProducto')
def mostrar_registro_producto():
    return render_template("form_registrar_producto.html")


@app.route('/reProducto', methods=['GET'])
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
@app.route('/eliminarProducto/<int:idProducto>', methods=['GET'])
def eliminar_producto(idProducto):
    producto = Producto.query.get(idProducto)
    #db.session.delete(producto)
    #db.session.commit()
    return redirect('/productos')

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


if __name__ == '__main__':
     app.run(port=5000, debug=True)