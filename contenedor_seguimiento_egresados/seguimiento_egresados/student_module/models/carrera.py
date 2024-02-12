from django.db import models

from ..validators import just_letters


class Carrera(models.Model):
    # id_carrera = models.IntegerField(primary_key=True)
    licenciatura = models.CharField(max_length=100, validators=[just_letters], null=True, blank=True)

    def __str__(self):
        return self.licenciatura
