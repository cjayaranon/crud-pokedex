from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *
# Create your views here.


class PokeSearch(TemplateView):
    template_name = "landing.html"
    model = Pokemons

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # get the default context data
        context['pokemon_details'] = self.model.objects.filter(id__contains=1) # add extra field to the context
        return context

    def post(self, request, *args, **kwargs):
        print(request.POST['search-bar'])
        # query_list = self.model.objects.filter(
        #     name=
        # )
        return render(request, self.template_name, {})



class AddNewPokemon(TemplateView):
    template_name = "add_new.html"