from flask import render_template

from app import app

@app.route('/')
@app.route('/index')
@app.route('/orders')
@app.route('/menu')
def index():
    return render_template('index.html', title = 'Home')
def orders():
    return render_template('orders.html', title = 'Orders')
