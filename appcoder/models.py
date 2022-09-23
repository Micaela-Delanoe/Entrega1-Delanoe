from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre= models.CharField(max_length=60)
    apellido= models.CharField(max_length=60)
    edad= models.IntegerField()

class Domicilio(models.Model):
    tipo= models.CharField(max_length=60)
    ciudad= models.CharField(max_length=60)
    pais= models.CharField(max_length=60)

class Mascota(models.Model):
    nombre= models.CharField(max_length=60)
    edad= models.IntegerField()
    animal= models.CharField(max_length=60)