# Generated by Django 4.2 on 2023-05-04 06:14

import django.core.validators
from django.db import migrations, models
import re
import student_module.models


class Migration(migrations.Migration):

    dependencies = [
        ('student_module', '0003_alter_student_fecha_ingreso_lic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='licenciatura',
            name='nombre_campus',
            field=models.CharField(blank=True, max_length=45, null=True, validators=[django.core.validators.RegexValidator('^[a-zA-ZñÑáéíóúÁÉÍÓÚ]+(?: [a-zA-ZñÑáéíóúÁÉÍÓÚ]+)*$', 'Sólo se permiten letras')]),
        ),
        migrations.AlterField(
            model_name='student',
            name='apellido_materno',
            field=models.CharField(blank=True, max_length=45, null=True, validators=[django.core.validators.RegexValidator('^[a-zA-ZñÑáéíóúÁÉÍÓÚ]+(?: [a-zA-ZñÑáéíóúÁÉÍÓÚ]+)*$', 'Sólo se permiten letras')]),
        ),
        migrations.AlterField(
            model_name='student',
            name='apellido_paterno',
            field=models.CharField(blank=True, max_length=45, null=True, validators=[django.core.validators.RegexValidator('^[a-zA-ZñÑáéíóúÁÉÍÓÚ]+(?: [a-zA-ZñÑáéíóúÁÉÍÓÚ]+)*$', 'Sólo se permiten letras')]),
        ),
        migrations.AlterField(
            model_name='student',
            name='fecha_nacimiento',
            field=models.DateField(blank=True, null=True, validators=[student_module.models.validate_age_range]),
        ),
        migrations.AlterField(
            model_name='student',
            name='licenciatura_fei',
            field=models.CharField(blank=True, choices=[('', 'Seleccione...'), ('Estadística', 'Estadística'), ('Ingeniería de Software', 'Ingeniería de Software'), ('Tecnologías Computacionales ', 'Tecnologías Computacionales'), ('Redes y Servicios de Cómputo ', 'Redes y Servicios de Cómputo')], max_length=100, null=True, validators=[django.core.validators.RegexValidator(message='El nombre solo debe contener letras y un espacio entre palabras', regex=re.compile('^[a-zA-ZáéíóúüñÁÉÍÓÚÜÑ]+(?: [a-zA-ZáéíóúüñÁÉÍÓÚÜÑ]+)*$'))]),
        ),
        migrations.AlterField(
            model_name='student',
            name='nombre',
            field=models.CharField(blank=True, max_length=45, null=True, validators=[django.core.validators.RegexValidator(message='El nombre solo debe contener letras y un espacio entre palabras', regex=re.compile('^[a-zA-ZáéíóúüñÁÉÍÓÚÜÑ]+(?: [a-zA-ZáéíóúüñÁÉÍÓÚÜÑ]+)*$'))]),
        ),
    ]
