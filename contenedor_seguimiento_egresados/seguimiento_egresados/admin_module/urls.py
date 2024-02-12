from django.urls import path
from .views import home, logout_view, detail_student
from .views import CustomLoginView
from django.conf import settings

app_name = 'admin_module'

urlpatterns = [
    path('%sloginadmin/' % settings.PATH_PREFIX, CustomLoginView.as_view(template_name="admin_module/login.html"),
         name="loginadmin"),
    path('%slogout_view/' % settings.PATH_PREFIX, logout_view, name='logout'),
    path('%shomeadmin/' % settings.PATH_PREFIX, home, name='home'),
    path('%sstudents/<str:enrollment>/' % settings.PATH_PREFIX, detail_student, name='student_detail'),
]
