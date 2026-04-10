from django.contrib import admin
from .models import Cancion, Artista

admin.site.register(Artista)
admin.site.register(Cancion)