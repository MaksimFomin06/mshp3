"""
URL configuration for first_django_dz project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
import my_site.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', my_site.views.index_page),
    path('riddle/', my_site.views.riddle),
    path('answer/', my_site.views.answer),
    path('multiply/', my_site.views.multiply),
]
