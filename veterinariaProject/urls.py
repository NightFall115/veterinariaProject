"""
URL configuration for veterinariaProject project.

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

from veterinariaApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.inicio,name='inicio'),
    ###     Dueño       ###
    path('crearDueño/',views.crearDueño,name='CrearDueño'),
    path('listarDueño/',views.listarDueño,name='MostrarDueño'),
    path('editarDueño/',views.editarDueño,name='EditarDueño'),
    path('eliminarDueño/<int:id>',views.eliminarDueño,name='EliminarDueño'),
    ###     Mascota     ###
    path('CrearMascota/',views.crearMascota,name='CrearMascota'),
    path('mostrarMascota/',views.listarMascota,name='MostrarMascota'),
    path('EditarMascota/',views.editarMascota,name='EditarMascota'),
    path('eliminarMascota/<int:id>',views.eliminarMascota,name='EliminarMascota'),
    ###     Cita        ###
    path('CrearCita/',views.crearMedica,name='CrearCita'),
    path('MostrarCita/',views.listarCita,name='MostrarCita'),
    path('EditarCita/',views.editarCita,name='EditarCita'),
    path('eliminarCita/<int:id>',views.eliminarCita,name='EliminarCita'),
    ###     Tratamiento     ###
    path('CrearTratamiento/',views.crearTratamiento,name='CrearTratamiento'),
    path('MostrarTratamiento/',views.listarTratamiento,name='MostrarTratamiento'),
    path('EditarTratamiento/',views.editarTratamiento,name='EditarTratamiento'),
    path('eliminarTratamiento/<int:id>',views.eliminarTratamiento,name='EliminarTratamiento'),
]
