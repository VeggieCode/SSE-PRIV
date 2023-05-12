from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Coordinator(models.Model):
    nombre_completo = models.CharField(max_length=100,null=True)
    carrera_asignada = models.CharField(max_length=100, null=True)
    usuario =  models.ForeignKey(User, on_delete=models.CASCADE, null=True)
