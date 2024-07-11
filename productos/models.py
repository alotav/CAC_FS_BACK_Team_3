from django.db import models

# Create your models here.
# subimos las img de cada producto a media/productos
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_length=10, decimal_places=2, max_digits=10)
    stock = models.PositiveIntegerField()
    imagen = models.ImageField(upload_to='productos/', default='productos/default.jpg')

    def __str__(self):
        return self.nombre
    
class ProductoNovedades(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='novedades/', default='productos/default.jpg')

    def __str__(self):
        return self.nombre
    
    