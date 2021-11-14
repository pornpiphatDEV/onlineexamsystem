"""onlineexamsystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from quizsystem import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('loginForm/', views.loginform, name='loginform'),
    path('register_optionsForm/', views.register_optionsform,
         name="register_optionsForm"),
    path('registerform_lecturer/', views.registerform__lecturer),
    path('registerform_student/', views.registerform_student),
    path('registerstudent/', views.registerstudent, name="registerstudent"),
    path('registerlecturer/', views.registerlecturer, name="registerlecturer"),
    path('login/', views.login, name="login"),
    path('student/', views.student, name="student"),
    path('lecturer/', views.lecturer, name="lecturer"),
    path('logout/', views.logout_view, name="logout")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
