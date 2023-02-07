import pokebase as pb
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'Saves all the Pokemon from PokeAPI into Dex-a-Poke.'

    def handle(self, *args, **kwargs):
        # data = 
        self.stdout.write(self.style.SUCCESS('Command created'))