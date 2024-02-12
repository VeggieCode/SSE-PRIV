import datetime

from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator
from django.db import models

from student_module.validators import alphanumeric, just_letters_blank, just_letters, only_email, \
    only_phone_number_mx, only_postal_code_mx

SEXOS = (('', 'Seleccione sexo'), ('M', 'Masculino'),
         # First one is the value of select option and second is the displayed value in option
         ('F', 'Femenino'), ('O', 'Prefiero no decirlo'))

MAX_YEAR = datetime.date.today().year - 4


def validate_age_range(value):
    today = datetime.date.today()
    age = today.year - value.year - ((today.month, today.day) < (value.month, value.day))
    if age < 20 or age > 40:
        raise ValidationError('La edad debe estar entre 20 y 40 años.')


class Student(models.Model):

    matricula = models.CharField(max_length=9, validators=[alphanumeric])
    nombre = models.CharField(max_length=45, blank=False, null=True, validators=[just_letters_blank])
    apellido_paterno = models.CharField(max_length=45, blank=False, null=True, validators=[just_letters])
    apellido_materno = models.CharField(max_length=45, blank=False, null=True, validators=[just_letters])
    sexo = models.CharField(max_length=10, choices=SEXOS, blank=False, null=True)
    fecha_nacimiento = models.DateField(blank=False, null=True, validators=[validate_age_range])
    fecha_ingreso_lic = models.IntegerField(blank=False, null=True, validators=[MaxValueValidator(MAX_YEAR)])
    licenciatura_fei = models.CharField(max_length=500, blank=True, null=True)
    correo = models.CharField(max_length=45, blank=False, null=True, validators=[only_email])
    correo_uv = models.CharField(max_length=45, blank=True, null=True, validators=[only_email])
    celular = models.CharField(max_length=10, validators=[only_phone_number_mx], blank=False, null=True)
    telefono = models.CharField(max_length=10, blank=True, null=True, validators=[only_phone_number_mx])
    twitter = models.CharField(max_length=45, blank=True, null=True)
    facebook = models.CharField(max_length=45, blank=True, null=True)
    linkedin = models.CharField(max_length=45, blank=True, default='')
    calle = models.CharField(max_length=45, blank=False, null=True)
    numero_exterior = models.IntegerField(null=True, blank=False)
    numero_interior = models.IntegerField(null=True, blank=True)
    colonia = models.CharField(max_length=45, blank=False, null=True)
    codigo_postal = models.CharField(max_length=5, blank=False, null=True, validators=[only_postal_code_mx])
    correo_alterno = models.CharField(max_length=45, blank=True, null=True, validators=[only_email])
    pre_egreso_abierto = models.BooleanField(default=False)
    post_egreso_abierto = models.BooleanField(default=False)
    nombre_ref_principal = models.CharField(max_length=100, blank=False, null=True)
    celular_ref_principal = models.CharField(max_length=10, validators=[only_phone_number_mx], blank=False, null=True)
    nombre_ref_auxiliar = models.CharField(max_length=100, blank=True, null=True)
    celular_ref_auxiliar = models.CharField(max_length=10, validators=[only_phone_number_mx], blank=True, null=True)
    estado = models.CharField(max_length=50, blank=False, null=True)
    municipio = models.CharField(max_length=50, blank=False, null=True)
    localidad = models.CharField(max_length=50, blank=False, null=True)
    pre_egreso_terminado = models.BooleanField(default=False)
    pre_egreso_fecha_fin = models.DateField(blank=False, null=True)

    def full_name(self):
        return self.nombre + ' ' + self.apellido_paterno + ' ' + self.apellido_materno
