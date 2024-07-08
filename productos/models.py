from django.db import models

# Create your models here.
class Producto:
    nombre = models.Charfield(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_length=10, decimal_places=2)
    stock = models.PositiveIntegerField()

    def __str__(self):
        return self.nombre