from django.apps import apps
from django.contrib import admin
from .models import *

dexapoke_models = apps.get_models()

for items in dexapoke_models:
    try:
        admin.site.register(items)
    except admin.sites.AlreadyRegistered:
        pass
