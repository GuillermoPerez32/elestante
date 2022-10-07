from django.shortcuts import render
from rest_framework import viewsets

from api.models import Libro, Modulo
from api.serializers import LibroSerializer, ModuloSerializer

from directorio.permissions import EsAdministrador, EsPlanificador, EsSecretario

# Create your views here.


class ModuloViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Modulo instances.
    """
    serializer_class = ModuloSerializer
    queryset = Modulo.objects.all()
    permission_classes = [EsAdministrador | EsSecretario]


class LibroViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Libro instances.
    """
    serializer_class = LibroSerializer
    queryset = Libro.objects.all()
    permission_classes = [EsAdministrador | EsPlanificador]
