from flask import Flask, render_template, url_for, redirect, request, Blueprint, jsonify

from alchemyClasses.Pedido import Pedido
from alchemyClasses.Usuario import Usuario
from alchemyClasses.__init__ import db
from alchemyClasses.Producto import Producto
from alchemyClasses.Conforma import Conforma
from alchemyClasses.Ordena import Ordena
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from controllers.ControladorUsuario import registro_cliente_blueprint, direccion_envio_blueprint, pago_blueprint
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
app.register_blueprint(direccion_envio_blueprint)
app.register_blueprint(pago_blueprint)
app.register_blueprint(productos_blueprint)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://'+DATABASE_USERNAME+':'+DATABASE_PASSWORD+'@'+DATABASE_HOST+'/'+DATABASE_NAME
app.config.from_mapping(
    SECRET_KEY='dev'
)

def create_app():
    db.init_app(app)
    return app

create_app()

#routes
@app.route('/')
def index():
    return render_template('index.html')

#create new product
@app.route('/products/create', methods=['GET', 'POST'])
def create_product():
    if request.method == 'POST':
        name = request.form['name']
        price = float(request.form['price'])
        description = request.form['description']
        amount_available = int(request.form['amount_available'])

        product = Product(name=name, price=price, description=description, amount_available=amount_available)
        db.session.add(product)
        db.session.commit()

        return redirect(url_for('index'))
    return render_template('create_product.html')

#list products
@app.route('/products')
def list_products():
    search_query = request.args.get('search', '')
    if search_query:
       products = Product.query.filter(Product.name.ilike(f'%{search_query}%')).all()
    else:
       products = Product.query.all()
    return render_template('list_products.html', products=products)

#eliminate product
@app.route('/products/eliminate/<int:product_id>', methods=['POST'])
def eliminate_product(product_id):
   product = Product.query.get_or_404(product_id)
   db.session.delete(product)
   db.session.commit()
   return redirect(url_for('list_products'))
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
    if request.method == "POST":
        return redirect(url_for("direccion_envio.direccion_envio"))
    else:
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

#run app
if __name__ == '__main__':
    app.app_context().push()
    db.create_all()
    app.run(debug=True)