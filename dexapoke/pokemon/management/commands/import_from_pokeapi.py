import requests as rqs
import time
from pokemon.models import Pokemons, PokemonType, PokemonAbility
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'Saves all the Pokemon from PokeAPI into Dex-a-Poke.'

    def get_query_count(*args):
        """
        Queries the API endpoint and gets the 'count' returned by
        the response object, for use in the same request
        but with parameter 'limit'.
        """
        pokeapi_url = "https://pokeapi.co/api/v2/"
        response_obj = rqs.get(pokeapi_url+args[0])
        data_obj = response_obj.json()

        if data_obj['count'] > 20:
            response_obj_2 = rqs.get(
                pokeapi_url+args[0],
                params={'limit':data_obj['count']}
            )
            data_obj = response_obj_2.json()
        
        return data_obj, args[1]


    def other_tables(addr, target_model):
        """
        Saves to db.sqlite3 the response objects returned by
        :classmethod: 'get_query_count'.
        """
        data_obj = Command.get_query_count(addr, target_model)
        # python3.10 use (data_obj['results'])
        for idx, items in enumerate(data_obj[0]['results']):
            db_entry = target_model.objects.get_or_create(
                id = idx+1,
                name = items['name']
            )


    def handle(self, *args, **kwargs):
        """
        Built-in classmethod for :class: 'Command'.
        Called by default upon invoking $python manage.py import_from_pokeapi
        in the terminal.
        """

        # get pokemon types
        Command.other_tables('type/', PokemonType)
        time.sleep(5)

        # get pokemon abilities
        Command.other_tables('ability/', PokemonAbility)
        time.sleep(5)

        # get, save, and associate pokemons
        # one-by-one request using NDEX
        for pokes in range(1, 30):
            pokemon = rqs.get(
                'https://pokeapi.co/api/v2/pokemon/'+str(pokes),
                verify=False
            )
            pokemon_data = pokemon.json()
            db_entry = Pokemons.objects.get_or_create(
                id = pokemon_data['id'],
                name = pokemon_data['name'],
                height = pokemon_data['height'],
                weight = pokemon_data['weight'],
                pokemon_type = pokemon_data['types'],
                pokemon_ability = pokemon_data['abilities']
            )
            time.sleep(3)

# evolution chain
# https://pokeapi.co/api/v2/evolution-chain/{id}/