from django.db import models
from django.db.models import DO_NOTHING

from student_module.validators import just_letters, only_decimals, alphanumeric

TITULADO_CHOICES = (('', 'Seleccione...'), ('Sí', 'Titulado'), ('No', 'No titulado'), ('En proceso', 'En proceso'))
TIPOINSCRIPCION = (('', 'Seleccione...'), ('Tiempo completo', 'Tiempo completo'), ('Tiempo parcial', 'Tiempo parcial'))


class Licenciatura(models.Model):
    # id_licenciatura = models.IntegerField(primary_key=True)
    nombre_campus = models.CharField(max_length=45, validators=[just_letters], null=True, blank=True)
    nombre_carrera = models.CharField(max_length=500, blank=True, null=True)
    anio_pestudios = models.CharField(max_length=45, blank=True, null=True)
    anio_inicio = models.CharField(max_length=25, blank=True, null=True)
    anio_fin = models.CharField(max_length=25, blank=True, null=True)
    org_ss = models.CharField(max_length=45, blank=True, null=True)
    fecha_inicioss = models.DateField(blank=True, null=True)
    fecha_finss = models.DateField(blank=True, null=True)
    titulado = models.CharField(max_length=10, choices=TITULADO_CHOICES, null=True, blank=True)
    promedio_final = models.FloatField(blank=True, null=True, validators=[only_decimals])
    tipo_inscripcion = models.CharField(max_length=25, choices=TIPOINSCRIPCION, null=True, blank=True)
    matricula = models.ForeignKey('student_module.student', on_delete=DO_NOTHING, db_column='matricula', validators=[alphanumeric],
                                  null=True)
