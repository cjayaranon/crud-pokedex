from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class PokeSearch(TemplateView):
    template_name = "landing.html"


class AddNewPokemon(TemplateView):
    template_name = "add_new.html"