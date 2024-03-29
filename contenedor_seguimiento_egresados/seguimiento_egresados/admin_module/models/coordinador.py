from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Coordinador(models.Model):
    nombre_completo = models.CharField(max_length=100, blank=True)
    carrera_asignada = models.CharField(max_length=100, blank=True)
    correo = models.CharField(max_length=45, blank=True)
    coordinador_general = models.BooleanField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.usuario.username
