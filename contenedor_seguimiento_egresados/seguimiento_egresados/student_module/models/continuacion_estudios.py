from django.db import models
from django.db.models import DO_NOTHING

from student_module.models.seleccion_carrera import SI_NO_CHOICES_NUMERIC
from student_module.validators import just_number, alphanumeric

TIPO_CONTINUACION_ESTUDIOS = (
    ('', 'Seleccione el tipo de continuación de estudios...'), ('Cursos cortos ', 'Cursos cortos'),
    ('Diplomado ', 'Diplomado'), ('Especialización', 'Especialización'), ('Maestría', 'Maestría'),
    ('Doctorado', 'Doctorado'), ('Otro', 'Otro'))
TIPO_INSTITUCION_CONTINUACION = (('', 'Seleccione el tipo de institución'), ('Pública ', 'Pública'),
                                 # First one is the value of select option and second is the displayed value in option
                                 ('Privada', 'Privada'), ('Otro', 'Otro'))


class ContinuacionEstudios(models.Model):
    # id_continuacion_estudios = models.IntegerField(primary_key=True)
    tipo_estudio_continuacion = models.CharField(max_length=45, choices=TIPO_CONTINUACION_ESTUDIOS, null=True,
                                                 blank=True)
    institucion = models.CharField(max_length=45, choices=TIPO_INSTITUCION_CONTINUACION, null=True, blank=True)
    nombre_programa = models.CharField(max_length=45, blank=True, null=True)
    conclusion_estudios = models.IntegerField(blank=True, null=True, choices=SI_NO_CHOICES_NUMERIC)
    obtencion_grado = models.IntegerField(blank=True, null=True, choices=SI_NO_CHOICES_NUMERIC)
    duracion_estudios_meses = models.IntegerField(blank=True, null=True, validators=[just_number])
    matricula = models.ForeignKey('Student', on_delete=DO_NOTHING, db_column='matricula',
                                  validators=[alphanumeric], null=True)
