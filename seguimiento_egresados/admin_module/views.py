from django.shortcuts import render, redirect
from .forms import CustomAuthenticationForm
from student_module.models import Student, Licenciatura
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.db import connection

# Create your views here.

class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm

@login_required
def home(request):
    students = Student.objects.all()
    datos = {'students': students}
    return render(request, 'admin_module/student_list.html', datos)

def logout_view(request):
    logout(request)
    return redirect('/login')