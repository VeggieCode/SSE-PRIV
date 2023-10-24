"""seguimiento_egresados URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views
from student_module.views import CustomPasswordResetCompleteView, CustomPasswordResetConfirmView, CustomPasswordResetDoneView, CustomPasswordResetView, CustomLoginView

handler404= views.custom_error_view
handler500= views.custom_error_view

urlpatterns = ([
    path('%s' % settings.PATH_PREFIX, CustomLoginView.as_view(template_name="student_module/login.html"), name="login"),
    path('%sadmin/clearcache/' % settings.PATH_PREFIX, include('clearcache.urls')),
    path('%sadmin/' % settings.PATH_PREFIX, admin.site.urls),
    path('', include('student_module.urls')),
    path('', include('admin_module.urls')),
    path('%spassword-reset/' % settings.PATH_PREFIX, CustomPasswordResetView.as_view(), name='password_reset'),
    path('%spassword-reset/done/' % settings.PATH_PREFIX, CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('%spassword-reset/confirm/<uidb64>/<token>/' % settings.PATH_PREFIX, CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('%spassword-reset/complete/' % settings.PATH_PREFIX, CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
])
#For serving static files in debug mode:
#+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)