from flask import render_template 
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template("home.html")

@app.route('/result')
def result():
	return render_template("result.html")