from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
#from controllers.ControladorUsuario import registra_cliente_blueprint

DATABASE_NAME = "micheladasatucasa"
DATABASE_USERNAME = "natalia" 
DATABASE_PASSWORD = "ati_desa15"
DATABASE_HOST = "localhost:3306"

app = Flask(__name__)
db = SQLAlchemy()
#app.register_blueprint(registra_cliente_blueprint)
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
    return render_template("registro_cliente.html")

if __name__ == '__main__':
     app.run(port=5000, debug=True)