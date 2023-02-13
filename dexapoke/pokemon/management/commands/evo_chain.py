import requests as rqs

def get_evo_chain(pokemon_data):
    evo_list = []

    # get pokemon > species > url
    pokemon_data_species = pokemon_data['species']
    pokemon_species = rqs.get(pokemon_data_species['url'])

    # get pokemon-species > evo-chain > url
    pokemon_species_details = pokemon_species.json()
    species_evo_chain = pokemon_species_details['evolution_chain']
    evo_chain = rqs.get(species_evo_chain['url'])

    # get evo-chain
    evo_chain_details = evo_chain.json()
    chain_evo1 = evo_chain_details['chain'] #list
    evo_list.append(chain_evo1['species']['name'])

    for items in chain_evo1['evolves_to']:
        evo_list.append(items['species']['name'])
        chain_evo2 = items['evolves_to'] #has inner species
        for items2 in chain_evo2:
            evo_list.append(items2['species']['name'])
            chain_evo3 = items2['evolves_to']
            for items3 in chain_evo3:
                evo_list.append(items3['evolves_to'])

    return evo_list

# if __name__ == '__main__':
#     get_evo_chain()