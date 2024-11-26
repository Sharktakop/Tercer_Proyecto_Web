from rest_framework import serializers

#se importa el modelo
from .models import Paquete

#se crea el serializador
class PaqueteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Paquete
        fields = ['id','nombre','marca','cantidadInventario','PrecioVenta','fechaCaducidad']