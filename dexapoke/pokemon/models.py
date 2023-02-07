from django.db import models


class Pokemons(models.Model):
    GENDER = (
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
    )

    # SPECIES = (
    #     ('MALE', 'Male'),
    #     ('FEMALE', 'Female'),
    # )

    # ABILITIES = (
    #     ('MALE', 'Male'),
    #     ('FEMALE', 'Female'),
    # )

    # POKEMON_TYPES = (
    #     ('MALE', 'Male'),
    #     ('FEMALE', 'Female'),
    # )

    # WEAKNESSES = (
    #     ('MALE', 'Male'),
    #     ('FEMALE', 'Female'),
    # )

    id = models.AutoField(primary_key = True)
    name = models.CharField(
        max_length = 50,
        blank = True,
        null = True
    )
    height = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)
    gender = models.CharField(
        max_length = 7,
        choices = GENDER,
        blank = True
    )
    category = models.CharField(
        max_length = 12,
        # choices = SPECIES,
        blank = True,
        null = True
    )
    abilities = models.CharField(
        max_length = 12,
        # choices = ABILITIES,
        blank = True,
        null = True
    )

    pokemon_type = models.CharField(
        max_length = 12,
        # choices = POKEMON_TYPES,
        blank = True,
        null = True
    )

    weaknesses = models.CharField(
        max_length = 12,
        # choices = WEAKNESSES,
        blank = True,
        null = True
    )

# Name (text)
# NDEX# (auto_id)
# Height (integer)
# Weight (integer)
# Gender (choice)
# Category (choice)
# Abilities (choice)
# Type (choice)
# Weaknesses (choice)
# Evolutions (choice; needs more info)
