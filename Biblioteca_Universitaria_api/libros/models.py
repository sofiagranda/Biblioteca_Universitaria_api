from django.db import models


from django.db import models

class Libro(models.Model):
    isbn = models.CharField(max_length=20, unique=True)
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    editorial = models.CharField(max_length=100)
    anio_publicacion = models.IntegerField()
    categoria = models.CharField(max_length=50)
    num_paginas = models.IntegerField()
    ubicacion = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)  # Ej: Disponible, Prestado
    copias_disponibles = models.IntegerField()

    def __str__(self):
        return f"{self.titulo} - {self.autor}"
