# Generated by Django 4.1.7 on 2023-04-11 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_module', '0005_student_localidad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='fecha_ingreso_lic',
            field=models.IntegerField(null=True),
        ),
    ]
