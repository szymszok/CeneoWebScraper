from flask import render_template
from app import app

@app.route('/')

@app.route('/<name>')
def index(name = 'World'):
    return render_template("index.html", name = name)

@app.route('/extract')
def extract():
    return render_template('extract.html')

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/products/<products_id>')
def product(product_id):
    return render_template('product.html', product_id=product_id)

@app.route('/charts/<product_id>')
def charts(product_id):
    return render_template('charts.html', product_id=product_id)

@app.route('/author')
def  author():
    return render_template('authour.html')
