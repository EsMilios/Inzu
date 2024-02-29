"""
URL configuration for Inzu project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

#extrae todas las vistas de inicioApp
from inicioApp.views import * 
from EstadisticasApp.views import *
from PerfilApp.views import *
from AhorrosApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    
    #rutas de inicioApp
    path('inicio/',inicioApp_inicio,name='inicioApp_inicio'),
    #rutas de estadisticas
    path('estadisticas/',Estadisticas_app,name='Estadisticas_app'),
    #ruta de ahorros
    path('ahorros/',ahorros_app,name='AhorrosApp'),
    #ruta de perfil
    path('perfil/',perfil_app,name='PerfilApp')
]
