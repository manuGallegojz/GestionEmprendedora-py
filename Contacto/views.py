from django.http import HttpResponse
from django.shortcuts import render
from .models import Contacto

def contactoForm(request):

    try:
        formulario = Contacto(
        nombre = request.GET["nombre"], 
        email = request.GET["email"], 
        asunto = request.GET["asunto"], 
        mensaje = request.GET["mensaje"], 
        ) 

        formulario.save()

        return render(request, 'pages/contacto.html')

    except:
        return render(request, 'pages/contacto.html')

def busquedaMensaje(request):

    return render(request, 'pages/buscar.html')

def resultado(request):

    if request.GET["nombre"]:

        nombre = request.GET["nombre"]
        mensajes = Contacto.objects.filter(nombre__icontains=nombre)

        return render(request, "pages/resultado.html", {"nombre" : nombre, "mensajes" : mensajes})

    else:

        return render(request, "pages/resultado.html")

