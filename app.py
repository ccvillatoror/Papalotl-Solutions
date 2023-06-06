from flask import Flask, render_template, url_for, redirect, request

from alchemyClasses.__init__ import db
from alchemyClasses.Producto import Producto
from controllers.ControladorPedido import pedidos_blueprint
from controllers.ControladorUsuario import registro_cliente_blueprint, direccion_envio_blueprint, pago_blueprint
from controllers.ControladorProducto import productos_blueprint
from controllers.ControladorSesion import login_usuario_blueprint, logout_usuario_blueprint

DATABASE_NAME = "micheladasatucasa"
DATABASE_USERNAME = "root"
DATABASE_PASSWORD = "root"
DATABASE_HOST = "localhost:3306"

app = Flask(__name__)
app.register_blueprint(registro_cliente_blueprint)
app.register_blueprint(login_usuario_blueprint)
app.register_blueprint(logout_usuario_blueprint)
app.register_blueprint(direccion_envio_blueprint)
app.register_blueprint(pago_blueprint)
app.register_blueprint(productos_blueprint)
app.register_blueprint(pedidos_blueprint)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://'+DATABASE_USERNAME+':'+DATABASE_PASSWORD+'@'+DATABASE_HOST+'/'+DATABASE_NAME
app.config.from_mapping(
    SECRET_KEY='dev'
)

def create_app():
    db.init_app(app)
    return app

create_app()

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
@app.route("/administrador")
def administrador():
    return render_template("administrador.html")

# ---------------------------
@app.route("/vendedor")
def vendedor():
    return render_template("vendedor.html")

# ---------------------------
@app.route("/registro-cliente", methods=["GET","POST"])
def registro_cliente():
    if request.method == "POST":
        return redirect(url_for("registro_cliente.registro_cliente"))
    else:
        return render_template("registro_cliente.html")

# ---------------------------
@app.route("/producto", methods=["GET","POST"])
def producto():
    return render_template("producto.html")

# ---------------------------
@app.route("/direccion-envio", methods=["GET", "POST"])
def dirección():
    if request.method == "POST":
        return redirect(url_for("direccion_envio.direccion_envio"))
    else:
        return render_template("direccion_envío.html")

# ---------------------------
@app.route("/pago", methods=["GET", "POST"])
def pago():
    return render_template("pago.html")

# ---------------------------
@app.route('/pedidos')
def mostrar_pedidos():
    return redirect(url_for("pedidos.mostrar_pedidos"))

# ---------------------------
@app.route('/pedido/<int:id_pedido>')
def mostrar_pedido(id_pedido):
    return redirect(url_for("pedidos.mostrar_pedido", id_pedido=id_pedido))

# ---------------------------
@app.route('/pedido/<int:id_pedido>/exito')
def estatus_actualizado(id_pedido):
    return redirect(url_for("pedidos.estatus_actualizado", id_pedido=id_pedido))

#run app
if __name__ == '__main__':
    app.app_context().push()
    db.create_all()
    app.run(debug=True)