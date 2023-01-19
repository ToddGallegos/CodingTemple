from app import app
from flask import render_template

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/pokemon')
def pokemon():
    return render_template('pokemon.html')