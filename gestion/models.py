from django.db import models

class Artista(models.Model):
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Cancion(models.Model):
    GENEROS = [
        ('Pop', 'Pop'),
        ('Rock', 'Rock'),
        ('Reggaeton', 'Reggaetón'),
        ('Jazz', 'Jazz'),
        ('Clasica', 'Clásica'),
        ('Electronica', 'Electrónica'),
        ('Hip Hop', 'Hip Hop'),
    ]
    titulo = models.CharField(max_length=200)
    duracion = models.DecimalField(max_digits=5, decimal_places=2, help_text="Duración en minutos")
    genero = models.CharField(max_length=50, choices=GENEROS)
    artista = models.ForeignKey(
        Artista,
        on_delete=models.CASCADE,
        related_name='canciones'
    )

    def __str__(self):
        return self.titulo