from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

from alchemyClasses.Producto import Producto
from controllers.gestionar_producto import registra_producto, actualizar_producto

DATABASE_NAME = "micheladasatucasa"
DATABASE_USERNAME = "natalia"
DATABASE_PASSWORD = "ati_desa15"
DATABASE_HOST = "localhost:3306"

app = Flask(__name__)
db = SQLAlchemy()
# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://natalia:ati_desa15@localhost:3306/prueba"

app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://' + DATABASE_USERNAME + ':' + DATABASE_PASSWORD + '@' + DATABASE_HOST + '/' + DATABASE_NAME
app.config.from_mapping(
    SECRET_KEY='dev'
)
db.init_app(app)

with app.app_context():
    try:
        # db.session.execute('SELECT 1')
        db.session.execute(text('SELECT 1'))
        print('\n\n----------- Connection successful ! -----------')
    except Exception as e:
        print('\n\n----------- Connection failed ! ERROR : ', e)


@app.route('/')
def hello():
    return render_template("index.html")


# ---------------------------
@app.route('/editarProducto/<int:producto_id>', methods=['GET'])
def mostrar_formulario_editar_producto(producto_id):
    producto = Producto.query.get(producto_id)
    return render_template('formulario_editar.html', producto=producto)


@app.route('/editarProducto/<int:producto_id>', methods=['POST'])
def modificar_producto(producto_id):
    actualizar_producto(producto_id)
    return 'Producto actualizado correctamente'


# ---------------------------
@app.route('/registrarProducto')
def mostrar_registro_producto():
    return render_template("form_registrar_producto.html")


@app.route('/reProducto', methods=['GET', 'POST'])
def registro_produto():
    registra_producto()
    return render_template("index.html")


# ---------------------------
@app.route('/productos')
def mostrar_productos():
    productos = Producto.query.all()
    return render_template('productos.html', productos=productos)


# ---------------------------
@app.route('/eliminar/<int:producto_id>', methods=['GET'])
def eliminar_producto(producto_id):
    producto = Producto.query.get(producto_id)
    db.session.delete(producto)
    db.session.commit()
    return 'Producto eliminado correctamente'


if __name__ == '__main__':
    app.run(port=5000, debug=True)
