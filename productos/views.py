from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request, "productos/inicio.html")

def novedades(request):
    return render(request, "productos/novedades.html")

def contacto(request):
    return render(request, "productos/contacto.html")

def nosotros(request):
    return render(request, "productos/nosotros.html")

def productos(request):
    return render(request, "productos/productos.html")