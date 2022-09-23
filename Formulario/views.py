from django.shortcuts import render
from .models import Formulario

def PresupuestoFormulario(request):

    try:
        formulario = Formulario(
        nombre = request.GET["nombre"], 
        apellido = request.GET["apellido"], 
        email = request.GET["email"], 
        whatsapp = request.GET["whatsapp"], 
        instagram = request.GET["instagram"], 
        localidad = request.GET["localidad"], 
        negocio = request.GET["negocio"], 
        actividad = request.GET["actividad"], 
        necesidad = request.GET["sobre_que_necesitas_presupuesto"], 
        juridiccion = request.GET["donde_vas_a_trabajar"], 
        exportar = request.GET["vendes_al_exterior"], 
        dependencia = request.GET["trabajas_bajo_relacion_de_dependencia"],
        precios = request.GET["vendes_algun_producto_por_arriba_de_$39.000"],
        expectativas = request.GET["esxpectativas"],
        comentarios = request.GET["comentarios"],
        ) 

        formulario.save()

        return render(request, 'pages/presupuesto.html')

    except:
        return render(request, 'pages/presupuesto.html')