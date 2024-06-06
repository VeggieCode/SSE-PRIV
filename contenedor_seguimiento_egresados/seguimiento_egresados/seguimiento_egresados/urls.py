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

handler404 = views.error_404_view
handler500 = views.custom_error_view

prefix = settings.PATH_PREFIX

urlpatterns = ([
    path(prefix, CustomLoginView.as_view(template_name="student_module/login.html"), name="login"),
    path('{prefix}admin/clearcache/'.format(prefix=prefix), include('clearcache.urls')),
    path('{prefix}admin/'.format(prefix=prefix), admin.site.urls, name='admin'),
    path(prefix, include('student_module.urls')),
    path(prefix, include('admin_module.urls')),
    path('{prefix}password-reset/'.format(prefix=prefix), CustomPasswordResetView.as_view(), name='password_reset'),
    path('{prefix}password-reset/done/'.format(prefix=prefix), CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('{prefix}password-reset/confirm/<uidb64>/<token>/'.format(prefix=prefix), CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('{prefix}password-reset/complete/'.format(prefix=prefix), CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
])

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)