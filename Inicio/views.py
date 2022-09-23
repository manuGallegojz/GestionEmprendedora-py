from django.shortcuts import render
from .models import Equipo

# Create your views here.

def Inicio(request):
    return render(request, 'index.html')

def EquipoFormulario(request):

    equipo = Equipo.objects.all()

    try:
        form = Equipo(
        nombre = request.GET["nombre"], 
        descripcion = request.GET["descripcion"], 
        instagram = request.GET["instagram"], 
        linkedin = request.GET["linkedin"], 
        ) 

        form.save()

        return render(request, 'pages/nuestro_equipo.html', {"equipo": equipo})

    except:
        return render(request, 'pages/nuestro_equipo.html', {"equipo": equipo})


def Servicios(request):
    return render(request, 'pages/servicios.html')