from django.shortcuts import render
from django.views.generic import TemplateView, UpdateView, CreateView
from .models import *
# Create your views here.


class PokeSearch(TemplateView):
    template_name = "landing.html"
    model = Pokemons

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # get the default context data
        model_objects = self.model.objects.all() # add extra field to the context
        
        # for items in model_objects:
        #     print(items)
        context['pokemon_details'] = model_objects
        context['pokemon_types'] = PokemonType.objects.all()
        return context

    def post(self, request, *args, **kwargs):

        # delete after testing
        print(request.POST)
        
        if (request.POST.get('search-bar')):
            query_list = self.model.objects.filter(
                name__contains = request.POST['search-bar']
            )
        elif (request.POST.get('dropdown-menu')):
            query_list = self.model.objects.filter(
                pokemon_type__contains = request.POST['dropdown-menu']
            )
        elif (request.POST.get('deleteBtn')):
            query_item = self.model.objects.get(
                id = request.POST['deleteBtn']
            )
            query_item.delete()
            query_list = self.model.objects.order_by('id')[:9]    
            
        return render(request, self.template_name, {'pokemon_details':query_list, 'pokemon_types':PokemonType.objects.all()})



class AddNewPokemon(CreateView):
    model = Pokemons
    template_name = "add_new.html"
    fields = '__all__'
    success_url = '/'



class PokemonUpdateView(UpdateView):
    model = Pokemons
    template_name = "edit_pokemon.html"
    fields = ['name', 'height', 'weight', 'pokemon_type', 'pokemon_ability']
    success_url = '/'

    def post(self, request, *args, **kwargs):
        return super(PokemonUpdateView, self).post(request, **kwargs)
            
    def form_valid(self, form):
        return super(PokemonUpdateView, self).form_valid(form)