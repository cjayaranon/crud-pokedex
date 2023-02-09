from django.db import models



class PokemonType(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(
        max_length =20,
        blank = True,
        null = True
    )



class PokemonAbility(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(
        max_length =20,
        blank = True,
        null = True
    )



class Pokemons(models.Model):
    """
    The Pokemons themselves;
    related loosely to :model:'PokemonAbility' and
    :model: 'PokemonType'.

    """
    id = models.AutoField(primary_key = True)
    name = models.CharField(
        max_length = 50,
        blank = True,
        null = True
    )
    height = models.IntegerField(default=0)
    
    weight = models.IntegerField(default=0)

    # cannot use ForeignKey because there can be multiple instances of these
    # objects in one Pokemon
    pokemon_type = models.CharField(
        max_length = 80,
        blank = True,
        null = True
    )

    pokemon_ability = models.CharField(
        max_length = 80,
        blank = True,
        null = True
    )

# Gender (choice)
# Category (choice)
# Weaknesses (choice)
# Evolutions (choice; needs more info)
