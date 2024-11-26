from django.db import models

# Create your models here.
class Paquete(models.Model):
    """
    Modelo que representa la estructura de datos de un registro correspondiente
    a los tipos de frituras/paquetes de una tienda local
    """
    nombre = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    cantidadInventario =  models.IntegerField()
    PrecioVenta = models.IntegerField()
    fechaCaducidad = models.DateField()
 