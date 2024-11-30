from django.urls import path

from veterinariaApp.views import crearDueño, editarDueño, eliminarDueño, listarDueño

urlpatterns = [
    path('crearDueño/',crearDueño,name='CrearDueño'),
    path('listarDueño/',listarDueño,name='MostrarDueño'),
    path('editarDueño/',editarDueño,name='EditarDueño'),
    path('eliminarDueño/<int:id>',eliminarDueño,name='EliminarDueño'),

    
]