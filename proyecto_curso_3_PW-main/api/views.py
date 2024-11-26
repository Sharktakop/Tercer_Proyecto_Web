from .models import Paquete
from rest_framework import viewsets
from rest_framework.response import Response
from .serial import PaqueteSerializer

# Create your views here.
class PaqueteViewSet(viewsets.ModelViewSet):
    """
    API-REST endpoint para el modelo paquete, admite
    GET, POST, PUT, PATCH, DELETE
    """
    queryset = Paquete.objects.all().order_by('cantidadInventario')
    serializer_class = PaqueteSerializer 