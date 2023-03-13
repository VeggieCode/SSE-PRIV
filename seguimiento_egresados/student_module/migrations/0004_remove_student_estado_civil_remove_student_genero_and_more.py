# Generated by Django 4.1.7 on 2023-03-13 19:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_module', '0003_alter_licenciatura_nombre_carrera'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='estado_civil',
        ),
        migrations.RemoveField(
            model_name='student',
            name='genero',
        ),
        migrations.AddField(
            model_name='student',
            name='celular_auxiliar',
            field=models.CharField(blank=True, max_length=10, null=True, validators=[django.core.validators.RegexValidator('^\\d{10}$', 'Sólo se permiten números de teléfono de 10 dígitos.')]),
        ),
        migrations.AddField(
            model_name='student',
            name='linkedin',
            field=models.CharField(default='', max_length=45),
        ),
        migrations.AddField(
            model_name='student',
            name='sexo',
            field=models.CharField(blank=True, choices=[('', 'Seleccione sexo'), ('M', 'Masculino'), ('F', 'Femenino')], max_length=10, null=True),
        ),
    ]
