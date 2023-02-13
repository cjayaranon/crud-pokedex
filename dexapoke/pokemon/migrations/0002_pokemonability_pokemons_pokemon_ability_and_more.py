# Generated by Django 4.1.6 on 2023-02-08 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PokemonAbility',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='pokemons',
            name='pokemon_ability',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='pokemons',
            name='pokemon_type',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]
