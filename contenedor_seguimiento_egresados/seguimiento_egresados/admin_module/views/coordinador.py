from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.shortcuts import render
from admin_module.models import Coordinador
from student_module.models.carrera import Carrera
from student_module.models.empleo import EmpleoDuranteEstudios
from student_module.models.student import Student


@login_required
def home(request):
    query = request.GET.get('search')
    degrees = Carrera.objects.all()
    user = request.user
    coordinator = Coordinador.objects.get(usuario=user)

    student_list = get_students(request)
    if query:
        object_list = student_list.filter(Q(nombre__icontains=query) | Q(matricula__icontains=query)).order_by(
            'matricula')
    else:
        object_list = student_list.order_by('matricula')  # Definir la cantidad de objetos por página
    objects_per_page = 10
    paginator = Paginator(object_list, objects_per_page)
    # Obtener la página solicitada por el usuario desde el parámetro GET
    page = request.GET.get('page')
    try:
        # Obtener los objetos a mostrar en la página actual
        students = paginator.page(page)
    except PageNotAnInteger:
        # Si el parámetro no es un número, mostrar la primera página
        students = paginator.page(1)
    except EmptyPage:
        # Si el número de página es mayor al total de páginas, mostrar la última página
        students = paginator.page(
            paginator.num_pages)  # Pasar la página actual, los objetos a mostrar y la cantidad total de objetos a la
        # plantilla HTML
    return render(request, 'admin_module/student_list.html',
                  {'page': page, 'students': students, 'degrees': degrees, 'coordinator': coordinator})


def get_students(request):
    user = request.user
    coordinator = Coordinador.objects.get(usuario=user)
    student_list = Student.objects.filter(licenciatura_fei=coordinator.carrera_asignada)
    if coordinator.coordinador_general:
        student_list = Student.objects.all()

    return student_list


def detail_student(request, enrollment):
    student = Student.objects.get(matricula=enrollment)
    job_during_degree = EmpleoDuranteEstudios.objects.filter(matricula=student.id).first()

    return render(request, 'admin_module/detail_student.html',
                  {'student': student, 'job_during_school': job_during_degree})
