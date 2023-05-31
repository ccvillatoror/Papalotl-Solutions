from flask import Flask, render_template, url_for, redirect, request, Blueprint, jsonify
from alchemyClasses.__init__ import db
from alchemyClasses.Producto import Producto
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

from controllers.ControladorUsuario import registro_cliente_blueprint
from controllers.ControladorProducto import productos_blueprint
from controllers.ControladorSesion import login_usuario_blueprint, logout_usuario_blueprint


DATABASE_NAME = "micheladasatucasa"
DATABASE_USERNAME = "natalia"
DATABASE_PASSWORD = "ati_desa15"
DATABASE_HOST = "localhost:3306"

app = Flask(__name__)
app.register_blueprint(registro_cliente_blueprint)

app.register_blueprint(login_usuario_blueprint)
app.register_blueprint(logout_usuario_blueprint)

app.register_blueprint(productos_blueprint)

app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://' + DATABASE_USERNAME + ':' + DATABASE_PASSWORD + '@' + DATABASE_HOST + '/' + DATABASE_NAME
app.config.from_mapping(
    SECRET_KEY='dev'
)

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
@app.route('/editarProducto/<int:idProducto>', methods=['GET'])
def editar_producto(idProducto):
    return redirect(url_for('editar_producto.editar_producto', idProducto=idProducto))

# ---------------------------
@app.route('/registrarProducto', methods=['GET', 'POST'])
def registro_producto():
    return redirect(url_for('registro_producto.agregar_producto'))

# ---------------------------
@app.route('/productos')
def mostrar_productos():
    return redirect(url_for('mostrar_productos.productos'))

# ---------------------------
@app.route('/producto/<int:idProducto>')
def mostrar_producto(idProducto):
    return redirect(url_for('mostrar_producto.mostrar_producto', idProducto=idProducto))

# ---------------------------
@app.route('/eliminarProducto/<int:idProducto>')
def eliminar_producto(idProducto):
    return redirect(url_for('eliminar_producto.eliminar_producto', idProducto=idProducto))

# ---------------------------
@app.route("/")
def home():
    productos = Producto.query.filter().all()
    return render_template("casa.html", productos=productos)

# ---------------------------
@app.route("/login", methods=["GET","POST"])
def login():
    return redirect(url_for("login.login_usuario"))

# ---------------------------
@app.route("/logout")
def logout():
    return redirect(url_for("logout.logout_usuario"))

# ---------------------------
@app.route("/registro-cliente", methods=["GET","POST"])
def registro_cliente():
    if request.method == "POST":
        return redirect(url_for("registro_cliente.registro_cliente"))
    else:
        return render_template("registro_cliente.html")

@app.route("/producto", methods=["GET","POST"])
def producto():
    return render_template("producto.html")

@app.route("/direccion-envio", methods=["GET", "POST"])
def dirección():
    return render_template("direccion_envío.html")

@app.route("/pago", methods=["GET", "POST"])
def pago():
    return render_template("pago.html")

# ---------------------------
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