from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

#create an instance of the Flask app and configure the SQLAlchemy database:
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'  # Replace with your database URI
db = SQLAlchemy(app)

#create database
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    price = db.Column(db.Float)
    description = db.Column(db.String(200))
    amount_available = db.Column(db.Integer)

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

#run app
if __name__ == '__main__':
    app.app_context().push()
    db.create_all()
    app.run(debug=True)