from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import viewsets, status
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
    # permission_classes = [EsAdministrador | EsSecretario]

    @action(detail=True, methods=['post'])
    def asignar(self, request: Request, pk=None):
        print(request.data)
        print('hola')
        modulo = self.get_object()
        print(modulo)
        user = User.objects.get(username=request.data['username'])
        print(user)
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
    serializer_class = LibroSerializer
    queryset = Libro.objects.all()
    permission_classes = [EsAdministrador | EsPlanificador]
