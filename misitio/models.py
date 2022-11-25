from django.db import models

# Create your models here.

class Cliente(models.Model):
    dni = models.CharField(max_length=9, primary_key=True)
    nombre = models.CharField(max_length=150, blank=False, null=False)
    fechaAlta = models.DateTimeField('Fecha Alta', blank=False, null=False)
    correo = models.CharField(max_length=150, blank=False, null=True)
    movil = models.CharField(max_length=14, blank=False, null=True)
