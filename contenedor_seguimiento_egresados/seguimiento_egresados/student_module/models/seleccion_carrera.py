from django.db import models
from django.db.models import DO_NOTHING

from student_module.validators import alphanumeric

TIPO_INSTITUCION = (('', 'Seleccione el tipo de institución'), ('Universidad Pública', 'Universidad Pública'),
                    # First one is the value of select option and second is the displayed value in option
                    ('Universidad Privada', 'Universidad Privada'),
                    ('Instituto Tecnológico y/o Politécnico Público', 'Instituto Tecnológico y/o Politécnico Público'),
                    ('Instituto Tecnológico Privado', 'Instituto Tecnológico Privado'), ('Otro', 'Otro'))
SI_NO_CHOICES_NUMERIC = ((1, "Sí"), (0, "No"),)


class SeleccionCarrera(models.Model):
    # id_seleccion_carrera = models.IntegerField(primary_key=True)
    primera_opcion_carrera = models.IntegerField(blank=True, null=True, choices=SI_NO_CHOICES_NUMERIC)
    eleccion_tipo_institucion = models.CharField(max_length=45, null=True, choices=TIPO_INSTITUCION, blank=True)
    primera_eleccion_institucion = models.IntegerField(blank=True, null=True, choices=SI_NO_CHOICES_NUMERIC)
    primera_eleccion_nombre = models.CharField(max_length=45, blank=True, null=True)
    razon_eleccion_institucion = models.CharField(max_length=45, blank=True, null=True)
    razon_eleccion_carrera = models.CharField(max_length=45, blank=True, null=True)
    matricula = models.ForeignKey('student_module.student', on_delete=DO_NOTHING, db_column='matricula',
                                  validators=[alphanumeric], null=True)
