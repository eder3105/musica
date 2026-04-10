from django import forms
from .models import Cancion, Artista

class ArtistaForm(forms.ModelForm):
    class Meta:
        model = Artista
        fields = ['nombre', 'nacionalidad']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'nacionalidad': forms.TextInput(attrs={'class': 'form-control'}),
        }

class CancionForm(forms.ModelForm):
    class Meta:
        model = Cancion
        fields = ['titulo', 'duracion', 'genero', 'artista']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'duracion': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'genero': forms.Select(attrs={'class': 'form-select'}),
            'artista': forms.Select(attrs={'class': 'form-select'}),
        }