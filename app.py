"""from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from controllers.ControladorUsuario import registra_cliente_blueprint

DATABASE_NAME = "micheladasatucasa"
DATABASE_USERNAME = "root"
DATABASE_PASSWORD = "root"
DATABASE_HOST = "localhost:3306"

app = Flask(__name__)
db = SQLAlchemy()
app.register_blueprint(registra_cliente_blueprint)
#app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://natalia:ati_desa15@localhost:3306/prueba"

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://'+DATABASE_USERNAME+':'+DATABASE_PASSWORD+'@'+DATABASE_HOST+'/'+DATABASE_NAME
app.config.from_mapping(
    SECRET_KEY='dev'
)
db.init_app(app)

with app.app_context():
    try:
        # db.session.execute('SELECT 1')
        db.session.execute(text('SELECT 1'))
        print('\n\n----------- Connection successful !')
    except Exception as e:
        print('\n\n----------- Connection failed ! ERROR : ', e)

@app.route('/')
def hello():
    return redirect(url_for('registro_cliente.registra_cliente'))

if __name__ == '__main__':
     app.run(port=5000, debug=True)"""
import json

from flask import Flask, render_template, url_for, redirect, request, Blueprint, jsonify
from controllers.ControladorUsuario import registro_cliente_blueprint
from controllers.login import loginBlueprint
from alchemyClasses.__init__ import db



app = Flask(__name__)
app.register_blueprint(registro_cliente_blueprint)
app.register_blueprint(loginBlueprint)

'''
Configuración base de datos temporal
'''
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///usuario.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

def create_app():
    db.init_app(app)
    return app

create_app()

@app.route("/")
def home():
    return render_template("casa.html")

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

@app.route("/producto", methods=["GET","POST"])
def producto():
    return render_template("producto.html")

@app.route("/direccion-envio", methods=["GET", "POST"])
def dirección():
    return render_template("direccion_envío.html")

@app.route("/pago", methods=["GET", "POST"])
def pago():
    return render_template("pago.html")

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

if __name__ == "__main__":
    app.run(port=5000, debug=True)