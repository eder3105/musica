from django.urls import path
from . import views

urlpatterns = [
    # Canciones
    path('canciones/', views.cancion_list, name='cancion_list'),
    path('canciones/nueva/', views.cancion_create, name='cancion_create'),
    path('canciones/editar/<int:pk>/', views.cancion_edit, name='cancion_edit'),
    path('canciones/eliminar/<int:pk>/', views.cancion_delete, name='cancion_delete'),
    # Artistas
    path('artistas/', views.artista_list, name='artista_list'),
    path('artistas/nuevo/', views.artista_create, name='artista_create'),
    path('artistas/editar/<int:pk>/', views.artista_edit, name='artista_edit'),
    path('artistas/eliminar/<int:pk>/', views.artista_delete, name='artista_delete'),
]