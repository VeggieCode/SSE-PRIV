from django.urls import path, include
from . import views
from .views import CustomLoginView, CustomPasswordResetCompleteView, CustomPasswordResetConfirmView, CustomPasswordResetDoneView, CustomPasswordResetView
from django.contrib.auth.views import (
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

from django.conf import settings

app_name = 'student_module'

urlpatterns = [
    path('%slogin/' % settings.PATH_PREFIX, CustomLoginView.as_view(template_name="student_module/login.html"), name="login"),
    path('%slogout_view/' % settings.PATH_PREFIX, views.logout_view, name='logout'),
    path('%shome/' % settings.PATH_PREFIX, views.home, name='home'),
    path('%sfinish/' % settings.PATH_PREFIX, views.finish, name='finish'),
    path('%ssignup/' % settings.PATH_PREFIX, views.signup, name='signup'),
    path('%sprivacy/' % settings.PATH_PREFIX, views.privacy_notice, name='privacy_notice'),
    path('%sstudent-info/' % settings.PATH_PREFIX, views.student_info, name='student_info'),
    path('%scareer-selection/' % settings.PATH_PREFIX, views.career_selection, name='career_selection'),
    path('%sbachelor/' % settings.PATH_PREFIX, views.bachelors_degree, name='bachelors_degree'),
    path('%sother-studies/' % settings.PATH_PREFIX, views.other_studies, name='other_studies'),
    path('%sjob-during-school/' % settings.PATH_PREFIX, views.job_during_school, name='job_during_school'),
    path('%sjob-search/' % settings.PATH_PREFIX, views.job_search, name='job_search'),
    path('%sjob-after-grad/' % settings.PATH_PREFIX, views.job_after_grad, name='job_after_grad'),
    path('%scurrent-job/' % settings.PATH_PREFIX, views.current_job, name='current_job'),
    path('%srecommendations/' % settings.PATH_PREFIX, views.recommendations, name='recommendations'),
    path('%spassword-reset/' % settings.PATH_PREFIX, CustomPasswordResetView.as_view(), name='password_reset'),
    path('%spassword-reset/done/' % settings.PATH_PREFIX, CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('%spassword-reset/confirm/<uidb64>/<token>/' % settings.PATH_PREFIX, CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('%spassword-reset/complete/' % settings.PATH_PREFIX, CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('%sgenerate-pdf/' % settings.PATH_PREFIX, views.generate_pdf, name='generate_pdf'),
    path('municipios/<int:id_estado>/', views.municipios_por_estado, name='municipios_por_estado'),
]