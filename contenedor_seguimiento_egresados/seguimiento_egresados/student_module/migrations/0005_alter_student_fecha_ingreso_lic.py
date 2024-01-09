# Generated by Django 4.2.2 on 2024-01-08 20:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_module', '0004_add_municipios'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='fecha_ingreso_lic',
            field=models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(2020)]),
        ),
    ]
