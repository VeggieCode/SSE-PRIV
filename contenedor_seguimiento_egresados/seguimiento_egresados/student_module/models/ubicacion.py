from django.db import models
from django.db.models import DO_NOTHING

from student_module.validators import alphanumeric


class Estados(models.Model):
    # id_estado = models.AutoField(primary_key=True)
    clave = models.CharField(max_length=25, blank=True, null=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    abrev = models.CharField(max_length=25, blank=True, null=True)
    activo = models.IntegerField()

    def __str__(self):
        return self.nombre


class Municipios(models.Model):
    # id_municipio = models.AutoField(primary_key=True)
    id_estado = models.ForeignKey('Estados', on_delete=models.CASCADE, db_column='id_estado', validators=[alphanumeric],
                                  null=True)
    clave = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
    activo = models.IntegerField()

    def __str__(self):
        return self.nombre


class Localidades(models.Model):
    # id_localidad = models.AutoField(primary_key=True)
    municipio = models.ForeignKey('Municipios', on_delete=DO_NOTHING, db_column='id_municipio',
                                  validators=[alphanumeric], null=True)
    clave = models.CharField(max_length=4)
    nombre = models.CharField(max_length=100)
    mapa = models.IntegerField()
    ambito = models.CharField(max_length=1)
    latitud = models.CharField(max_length=20)
    longitud = models.CharField(max_length=20)
    lat = models.DecimalField(max_digits=10, decimal_places=7)
    lng = models.DecimalField(max_digits=10, decimal_places=7)
    altitud = models.CharField(max_length=15)
    carta = models.CharField(max_length=10)
    poblacion = models.IntegerField()
    masculino = models.IntegerField()
    femenino = models.IntegerField()
    viviendas = models.IntegerField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
