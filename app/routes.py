from flask import render_template

from app import app

@app.route('/')
@app.route('/index')
@app.route('/orders')
@app.route9'/menu')
def index():
    return render_template('index.html', title = 'Home')
