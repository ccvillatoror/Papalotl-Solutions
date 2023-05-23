import json

from flask import Flask, render_template, url_for, redirect, request, Blueprint, jsonify
from controllers.ControladorUsuario import registro_cliente_blueprint
from controllers.login import loginBlueprint
from alchemyClasses.__init__ import db
from sqlalchemy import text

DATABASE_NAME = "micheladasatucasa"
DATABASE_USERNAME = "root"
DATABASE_PASSWORD = "root"
DATABASE_HOST = "localhost:3306"

app = Flask(__name__)
app.register_blueprint(registro_cliente_blueprint)
app.register_blueprint(loginBlueprint)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://'+DATABASE_USERNAME+':'+DATABASE_PASSWORD+'@'+DATABASE_HOST+'/'+DATABASE_NAME
app.config.from_mapping(
    SECRET_KEY='dev'
)

db.init_app(app)

@app.route("/")
def home():
    pedidos = db.session.execute(text('SELECT * FROM pedido WHERE estatus'))
    return render_template("pedidos.html", pedidos=pedidos)

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

if __name__ == "__main__":
    app.run(port=5000, debug=True)