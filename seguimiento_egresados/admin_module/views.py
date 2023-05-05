from django.shortcuts import render, redirect
from .forms import CustomAuthenticationForm
from student_module.models import Student, Licenciatura
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.db import connection
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.from django.contrib import messages
from django.contrib import messages
from django.db.models import Q
from .models import Coordinator
class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    def form_valid(self, form):
        # Obtener el usuario autenticado
        user = form.get_user()
        try:
            coordinator = Coordinator.objects.get(usuario=user)
        except Coordinator.DoesNotExist:
            coordinator = None
        if coordinator is None:
            form = CustomAuthenticationForm()
            return self.form_invalid(form)
        # limpiar el formulario
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.method == 'POST':
            # Si el formulario fue enviado por POST, mostramos el mensaje de error
            context['show_alert'] = True
        return context

#@login_required
def home(request):
    query = request.GET.get('search')
    if query:
        object_list = Student.objects.filter(
            Q(nombre__icontains=query) |
            Q(matricula__icontains=query) 
        ).order_by('matricula')
    else:
        object_list = Student.objects.all().order_by('matricula')
        # Definir la cantidad de objetos por página
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
        students = paginator.page(paginator.num_pages)
        # Pasar la página actual, los objetos a mostrar y la cantidad total de objetos a la plantilla HTML
    return render(request,  'admin_module/student_list.html', {'page': page, 'students': students})
    '''students = Student.objects.all()
        datos = {'students': students}
        return render(request, 'admin_module/student_list.html', datos)'''

def logout_view(request):
    logout(request)
    return redirect('/login')

def detail_student(request, enrollment):
    student = Student.objects.get(matricula=enrollment)
    return render(request, 'admin_module/detail_student.html', {'student': student})