from app import app
from flask import render_template, request, redirect, url_for, flash
from .forms import PokemonCatcherForm, SignUpForm, SignInForm
import requests

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/pokemon', methods=["GET", "POST"])
def pokemon():
    form = PokemonCatcherForm()
    if request.method == "POST":
        if form.validate():
            pokemon_name = form.pokemon_name.data
            
            def pokemon_info(p_name):
                response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{p_name.lower()}')
                if response.ok:
                    my_pokemon = {'pokemon_name': response.json()['forms'][0]['name'], 
                                'base_hp': response.json()['stats'][0]['base_stat'], 
                                'base_attack': response.json()['stats'][1]['base_stat'], 
                                'base_defense': response.json()['stats'][2]['base_stat'], 
                                'base_experience': response.json()['base_experience'], 
                                'ability_name': response.json()['abilities'][0]['ability']['name'], 
                                'front_shiny_sprite': response.json()['sprites']['front_shiny']}
                    return my_pokemon

            the_pokemon = pokemon_info(pokemon_name)
            form.pokemon_name.data = ''
            
            return render_template('pokemon.html', form = form, the_pokemon = the_pokemon)
        
    elif request.method == "GET":
        return render_template('pokemon.html', form = form)
    
@app.route('/mypokemon')
def mypokemon():
    return render_template('mypokemon.html')

@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    form = SignUpForm()
    if request.method == "POST":
        if form.validate():
            user_name = form.user_name.data
            email = form.email.data
            password = form.password.data
            
            # ADD USER TO DATABASE
            flash("You created an account. Please log in.")
            return redirect('/signin')
        else:
            flash("Invalid input. Please try again.")
            return render_template('signup.html', form = form)
    
    elif request.method == "GET":
        return render_template('signup.html', form = form)

@app.route('/signin', methods = ['GET', 'POST'])
def signin():
    form = SignInForm()
    if request.method == "POST":
        if form.validate():
            user_name = form.user_name.data
            password = form.password.data
            
        return render_template('signin.html', form = form)
    
    elif request.method == 'GET':
        return render_template('signin.html', form = form)