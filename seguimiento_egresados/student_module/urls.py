from django.urls import path, include
from . import views
from .views import CustomLoginView, CustomPasswordResetCompleteView, CustomPasswordResetConfirmView, CustomPasswordResetDoneView, CustomPasswordResetView
from django.contrib.auth.views import (
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView,
    PasswordResetCompleteView
)
from seguimiento_egresados import settings

app_name = 'student_module'

urlpatterns = [
    path('login/', CustomLoginView.as_view(template_name="student_module/login.html"), name="login"),
    path('logout_view/', views.logout_view, name='logout'),
    path('home/', views.home, name='home'),
    path('finish/', views.finish, name='finish'),
    path('signup/', views.signup, name='signup'),
    path('privacy/', views.privacy_notice, name='privacy_notice'),
    path('student-info/', views.student_info, name='student_info'),
    path('career-selection/', views.career_selection, name='career_selection'),
    path('bachelor/', views.bachelors_degree, name='bachelors_degree'),
    path('other-studies/', views.other_studies, name='other_studies'),
    path('job-during-school/', views.job_during_school, name='job_during_school'),
    path('job-search/', views.job_search, name='job_search'),
    path('job-after-grad/', views.job_after_grad, name='job_after_grad'),
    path('current-job/', views.current_job, name='current_job'),
    path('recommendations/', views.recommendations, name='recommendations'),
    path('password-reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset/confirm/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset/complete/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('generate-pdf/', views.generate_pdf, name='generate_pdf'),
]