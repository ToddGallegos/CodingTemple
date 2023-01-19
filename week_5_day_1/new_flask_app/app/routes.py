from app import app
from flask import render_template, request, redirect, url_for
from .forms import PokemonCatcherForm
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