import requests

def pokemon_info(p_name):
    
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{p_name}')
    
    if response.ok:
        my_pokemon = {'pokemon_name': response.json()['forms'][0]['name'], 
                    'base_hp': response.json()['stats'][0]['base_stat'], 
                    'base_attack': response.json()['stats'][1]['base_stat'], 
                    'base_defense': response.json()['stats'][2]['base_stat'], 
                    'base_experience': response.json()['base_experience'], 
                    'ability_name': response.json()['abilities'][0]['ability']['name'], 
                    'front_shiny_sprite': response.json()['sprites']['front_shiny']}
        return my_pokemon
    else:
        return "The Pokemon you're looking for does not exist."