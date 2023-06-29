from django.urls import path
from . import views
from .views import CustomLoginView

app_name = 'admin_module'

urlpatterns = [
    path('loginadmin/', CustomLoginView.as_view(template_name="admin_module/login.html"), name="loginadmin"),
    path('logout_view/', views.logout_view, name='logout'),
    path('homeadmin/', views.home, name='home'),
    path('students/<str:enrollment>/', views.detail_student, name='student_detail'),
]