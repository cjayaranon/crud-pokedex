from django.http import HttpRequest
from django.test import TestCase
from django.urls import resolve, reverse
from .models import *

class HomePageTest(TestCase):
    """
    Tests all features found in the url: home
    """

    def test_uses_template_and_shows_pokemons(self):
        pokemon_type = PokemonType.objects.create(name='fire')
        pokemon = Pokemons.objects.create(
            name = 'test-edit-pokemon',
            height = 0,
            weight = 55,
            pokemon_type = 'fire',
            pokemon_ability = ['dodge','fire-breathing'],
            pokemon_evolution ='Jigglypuff'
        )
        response = self.client.get(
            '/',
            data={
                'pokemon_details': pokemon,
                'pokemon_types': pokemon_type
            }
        )
        self.assertEqual(response.status_code, 200)
        template_list = ['base.html','landing.html','header.html']
        for templates in template_list:
            self.assertTemplateUsed(response, templates , 'Wrong template used')

    def test_can_handle_search_POST(self):
        pokemon = Pokemons.objects.create(
            name = 'test-edit-pokemon',
            height = 0,
            weight = 55,
            pokemon_type = 'fire',
            pokemon_ability = ['dodge','fire-breathing'],
            pokemon_evolution ='Jigglypuff'
        )
        response = self.client.post(
            '/',
            data={'search-bar': 'test'}
        )
        self.assertEqual(response.status_code, 200, 'Pokemon not searched')

    def test_can_handle_filter_POST(self):
        pokemon_type = PokemonType.objects.create(name='fire')
        response = self.client.post(
            '/',
            data={
                'dropdown-menu': 'fire'
            }
        )
        self.assertEqual(response.status_code, 200, 'Pokemon not filtered')

    def test_pokemon_delete_POST(self):
        pokemon = Pokemons.objects.create(
            name = 'test-edit-pokemon',
            height = 0,
            weight = 55,
            pokemon_type = 'fire',
            pokemon_ability = ['dodge','fire-breathing'],
            pokemon_evolution ='Jigglypuff'
        )
        
        response = self.client.post(
            '/',
            data={'deleteBtn':'1'}
        )
        self.assertEqual(response.status_code, 200, 'Pokemon not deleted')


class AddNewPokemonTest(TestCase):
    """
    Tests the 'add new' feature
    """

    def test_saves_new_pokemon(self):
        response = self.client.post(
            reverse('addNewPokemon'),
            data={
                'name':'test-pokemon',
                'height':'50',
                'weight':'55',
                'pokemon_type':'fire',
                'pokemon_ability':['dodge','fire-breathing'],
                'pokemon_evolution':'Jigglypuff'
            }
        )
        self.assertEqual(response.status_code, 302, 'Pokemon not saved')


class EditPokemonTest(TestCase):
    """
    Tests the 'edit' feature
    """
    
    def test_edit_pokemon(self):
        update_data = {
            'name':'test-pokemon',
            'height':50,
            'weight':55,
            'pokemon_type':'fire',
            'pokemon_ability':['dodge','fire-breathing'],
            'pokemon_evolution':'Jigglypuff'
        }
        pokemon = Pokemons.objects.create(
            name = 'test-edit-pokemon',
            height = 0,
            weight = 55,
            pokemon_type = 'fire',
            pokemon_ability = ['dodge','fire-breathing'],
            pokemon_evolution ='Jigglypuff'
        )
        response = self.client.post(
            reverse('edit', kwargs={'pk':pokemon.id}),
            data=update_data
        )
        self.assertEqual(response.status_code, 302)
        pokemon.refresh_from_db()
        self.assertEqual(pokemon.height, 50, 'Pokemon not edited')