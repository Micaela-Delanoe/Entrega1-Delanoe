from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from appcoder.forms import *
from proyecto1.appcoder.models import Domicilio, Usuario, Mascota
from django import forms

# Create your views here.

def usuarioFormulario(request):
    if request.method == "POST":
        formulario1 = usuarioFormulario(request.POST)

        if formulario1.is_valid():
            info =formulario1.cleaned_data
            usuario= Usuario(nombre= info["nombre"], apellido= info["apellido"], edad=info["edad"])

            usuario= Usuario(nombre=request.POST["nombre"], apellido=request.POST["apellido"], edad= request.POST["edad"])
            usuario.save()
        return render(request, "appcoder/inicio.html")

    else:
        formulario1= usuarioFormulario()

    return render(request, "appcoder/usuarioFormulario.html", {"form1": formulario1})

def domicilioFormulario(request):
    if request.method == "POST":
        formulario2 = domicilioFormulario(request.POST)

        if formulario2.is_valid():
            info =formulario2.cleaned_data
            domicilio= Domicilio(tipo= info["tipo"], pais= info["pais"], ciudad=info["ciudad"])

            domicilio= Domicilio(tipo=request.POST["tipo"], pais=request.POST["pais"], ciudad= request.POST["ciudad"])
            domicilio.save()
        return render(request, "appcoder/inicio.html")

    else:
        formulario2= domicilioFormulario()
    
    return render(request, "appcoder/domicilioFormulario.html", {"form2": formulario2})

def mascotaFormulario(request):
    if request.method == "POST":
        formulario3 = mascotaFormulario(request.POST)
        if formulario3.is_valid():
            info= formulario3.cleaned_data
            mascota= Mascota(nombre= info["nombre"], edad= info["edad"], animal=info["animal"])

            mascota= Mascota(nombre=request.POST["nombre"], edad=request.POST["edad"], animal= request.POST["animal"])
            mascota.save()
        return render(request, "appcoder/inicio.html")

    else:
        formulario3= mascotaFormulario()

    return render(request, "appcoder/mascotaFormulario.html", {"form3": formulario3})


def busquedaNombreU(request):
    return render(request, "appcoder/inicio.html")

def resultados(request):

    if request.GET["nombre"]:
        usuario=request.GET["nombre"]
        usuarios= Usuario.objects.filter(nombre__icontains=nombre)
        return render(request, "appcoder/inicio.html", {'nombre': nombre, 'apellido': apellido, 'edad': edad})
    
    else:
        respuesta= "No enviaste los datos"

    return HttpResponse(respuesta)