# Generated by Django 4.1.7 on 2023-04-12 22:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_module', '0007_remove_student_celular_referencia_auxiliar_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='numero',
        ),
    ]
