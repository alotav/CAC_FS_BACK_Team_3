from django.contrib import admin
from .models import Producto, ProductoNovedades

# Register your models here.
admin.site.register(Producto)
admin.site.register(ProductoNovedades)