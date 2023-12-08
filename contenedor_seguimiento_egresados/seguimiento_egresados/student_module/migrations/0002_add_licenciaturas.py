from django.db import migrations

licenciaturas = ['Estadística', 'Ingeniería de Software', 'Tecnologías Computacionales', 'Redes y Servicios de Cómputo']


def add_carreras(apps, _):
    carrera = apps.get_model('student_module', 'Carrera')
    for licenciatura in licenciaturas:
        carrera.objects.create(licenciatura=licenciatura)


class Migration(migrations.Migration):
    dependencies = [
        ('student_module', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_carreras),
    ]
