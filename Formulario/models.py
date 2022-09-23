from django.db import models

# Create your models here.

class Formulario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    whatsapp = models.CharField(max_length=150)
    instagram = models.CharField(max_length=200)
    localidad = models.CharField(max_length=100)
    negocio = models.CharField(max_length=100)
    actividad = models.TextField()
    necesidad = models.CharField(max_length=100)
    juridiccion = models.CharField(max_length=100)
    exportar = models.CharField(max_length=100)
    dependencia = models.CharField(max_length=100)
    precios = models.CharField(max_length=100)
    expectativas = models.TextField()
    comentarios = models.TextField()