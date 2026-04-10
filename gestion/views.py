from django.shortcuts import render, get_object_or_404, redirect
from .models import Cancion, Artista
from .forms import CancionForm, ArtistaForm

# ──────────── CANCIONES ────────────

def cancion_list(request):
    canciones = Cancion.objects.all()
    return render(request, 'gestion/cancion_list.html', {'canciones': canciones})

def cancion_create(request):
    form = CancionForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('cancion_list')
    return render(request, 'gestion/form.html', {'form': form, 'titulo': 'Nueva Canción'})

def cancion_edit(request, pk):
    cancion = get_object_or_404(Cancion, pk=pk)
    form = CancionForm(request.POST or None, instance=cancion)
    if form.is_valid():
        form.save()
        return redirect('cancion_list')
    return render(request, 'gestion/form.html', {'form': form, 'titulo': 'Editar Canción'})

def cancion_delete(request, pk):
    cancion = get_object_or_404(Cancion, pk=pk)
    if request.method == 'POST':
        cancion.delete()
        return redirect('cancion_list')
    return render(request, 'gestion/confirm_delete.html', {'objeto': cancion, 'tipo': 'canción'})

# ──────────── ARTISTAS ────────────

def artista_list(request):
    artistas = Artista.objects.all()
    return render(request, 'gestion/artista_list.html', {'artistas': artistas})

def artista_create(request):
    form = ArtistaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('artista_list')
    return render(request, 'gestion/form.html', {'form': form, 'titulo': 'Nuevo Artista'})

def artista_edit(request, pk):
    artista = get_object_or_404(Artista, pk=pk)
    form = ArtistaForm(request.POST or None, instance=artista)
    if form.is_valid():
        form.save()
        return redirect('artista_list')
    return render(request, 'gestion/form.html', {'form': form, 'titulo': 'Editar Artista'})

def artista_delete(request, pk):
    artista = get_object_or_404(Artista, pk=pk)
    if request.method == 'POST':
        artista.delete()
        return redirect('artista_list')
    return render(request, 'gestion/confirm_delete.html', {'objeto': artista, 'tipo': 'artista'})