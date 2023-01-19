from app import app
from flask import render_template
from .forms import PokemonCatcherForm

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/pokemon', methods=["GET", "POST"])
def pokemon():
    form = PokemonCatcherForm()
    return render_template('pokemon.html', form = form)