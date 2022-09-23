from django.urls import path
from . import views

urlpatterns = [
    path('inicio/', views.Inicio),
    path('nuestro_equipo/', views.EquipoFormulario),
    path('servicios/', views.Servicios),
]
