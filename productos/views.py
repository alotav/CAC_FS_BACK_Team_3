from django.shortcuts import render
from .models import Producto
from .models import ProductoNovedades


# Create your views here.

def inicio(request):
    novedades = ProductoNovedades.objects.all()
    return render(request, "productos/inicio.html", {'novedades': novedades})

def contacto(request):
    return render(request, "productos/contacto.html")

def nosotros(request):
    return render(request, "productos/nosotros.html")

def productos(request):
    productos = Producto.objects.all()
    return render(request, "productos/productos.html", {'productos': productos})

def novedades(request):
    primer_novedad = ProductoNovedades.objects.first()  # Obtener la primera novedad
    todas_novedades = ProductoNovedades.objects.exclude(pk=primer_novedad.pk)  # Todas las demás novedades
    return render(request, "productos/novedades.html", {'primer_novedad': primer_novedad, 'todas_novedades': todas_novedades})

# def inicio(request):
#     # Obtener los últimos 3 artículos de ProductoNovedades ordenados por fecha de creación descendente
#     ultimas_novedades = ProductoNovedades.objects.order_by('-id')[:3]  # Assuming 'id' gives the latest entries
#     context = {
#         'ultimas_novedades': ultimas_novedades,
#     }
#     return render(request, "productos/inicio.html", context)

