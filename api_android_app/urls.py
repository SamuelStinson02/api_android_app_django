"""api_android_app URL Configuration

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
    1. Import to include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# Importamos 'DefaultRouter' de Django REST Framework y la vista 'jugos'
from rest_framework.routers import DefaultRouter
from jugos import views as jugos_views

router = DefaultRouter()
router.register(r'jugos', jugos_views.JugosViewSet, basename='jugos')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
