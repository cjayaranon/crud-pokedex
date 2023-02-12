import requests as rqs

def get_type(pokemon_data):
    type_list = []

    pokemon_type = pokemon_data['types']
    for items in pokemon_type:
        type_list.append(items['type']['name'])

    return type_list

# if __name__ == '__main__':
#     get_type()