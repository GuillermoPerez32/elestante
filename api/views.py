from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import viewsets, status, views
from rest_framework.decorators import action

from api.models import Libro, Modulo
from api.serializers import LibroSerializer, ModuloSerializer

from directorio.permissions import EsAdministrador, EsPlanificador, EsSecretario
from directorio.models import User
# Create your views here.


class ModuloViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Modulo instances.
    """
    serializer_class = ModuloSerializer
    queryset = Modulo.objects.all()
    filterset_fields = {
        'categoria':['icontains']
    }
    permission_classes = [EsAdministrador | EsSecretario]

    def create(self, request: Request, *args, **kwargs):
        print(*request.data)
        return super().create(request, *args, **kwargs)

    @action(detail=True, methods=['post'])
    def asignar(self, request: Request, pk=None):
        modulo = self.get_object()
        user = User.objects.get(username=request.data.get('username'))
        modulo.usuarios.add(user)
        return Response(status=status.HTTP_200_OK)
        # try:
        # except Exception:
        #     print(Exception)
        #     return Response(status=status.HTTP_400_BAD_REQUEST)

class LibroViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Libro instances.
    """

    @action(detail=True, methods=['post'])
    def asignar(self, request: Request, pk=None):
        libro = self.get_object()
        user = User.objects.get(username=request.data.get('username'))
        libro.usuarios.add(user)
        return Response(status=status.HTTP_200_OK)
        # try:
        # except Exception:
        #     print(Exception)
        #     return Response(status=status.HTTP_400_BAD_REQUEST)

    serializer_class = LibroSerializer
    queryset = Libro.objects.all()
<<<<<<< HEAD
    filterset_fields = {
        'asignatura':['icontains']
    }
=======
    filterset_fields = ['asignatura']
>>>>>>> e06a071c917c46cecfe827b81b957d016172f3ea
    permission_classes = [EsAdministrador | EsPlanificador]
