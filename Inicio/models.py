from django.db import models

class Equipo(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    instagram = models.CharField(max_length=250)
    linkedin = models.CharField(max_length=250)