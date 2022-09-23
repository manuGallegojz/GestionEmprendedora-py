from django.urls import path
from . import views

urlpatterns = [
    path('contacto/', views.contactoForm),
    path('buscar/', views.busquedaMensaje),
    path('resultado/', views.resultado),
]
