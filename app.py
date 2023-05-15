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

from flask import Flask, render_template, url_for, redirect, request

from alchemyClasses.Pedido import Pedido

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("casa.html")

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        nombre = request.form["nombre"]
        total = request.form["total"]
        estatus = request.form["estatus"]
        """pedido = {
            "nombre":    request.form["nombre"],
            "total": request.form["total"],
            "estatus": request.form["estatus"],
        }"""
        #print("pedido recien hecho:", pedido)
        #fecha = request.form["fecha"]
        #pedido = Pedido(total,estatus)
        #pedido.fecha = fecha
        return redirect(url_for("user", usr=nombre))
    else:
        return render_template("prueba.html")

#%201?ttl=100&stts=Estatus&fch=2023-05-14
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