"""djangolevelfive URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from user_password import views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', views.base, name='base'),
    path('index/', views.index, name='index'),
    path('user_password/', include('user_password.urls')),
    path('logout/', views.user_logout, name='logout'),
    path('special/', views.special, name='special'),
    path('colorpicker/', views.colorpicker, name='colorpicker')
]
