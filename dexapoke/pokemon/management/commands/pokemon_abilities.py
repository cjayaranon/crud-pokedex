import requests as rqs

def get_ability(pokemon_data):
    ability_list = []

    # get pokemon > ability
    pokemon_ability = pokemon_data['abilities']
    for items in pokemon_ability:
        ability_list.append(items['ability']['name'])

    return ability_list

# if __name__ == '__main__':
#     get_ability()