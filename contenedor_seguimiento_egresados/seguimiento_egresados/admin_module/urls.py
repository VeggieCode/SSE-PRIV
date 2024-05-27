from django.urls import path
from .views import home, logout_view, detail_student
from .views import CustomLoginView
from django.conf import settings

app_name = 'admin_module'

urlpatterns = [
    path('loginadmin/', CustomLoginView.as_view(template_name="admin_module/login.html"),
         name="loginadmin"),
    path('logout_view/', logout_view, name='logout'),
    path('homeadmin/', home, name='home'),
    path('students/<str:enrollment>/', detail_student, name='student_detail'),
]
