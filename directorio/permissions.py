from rest_framework.permissions import BasePermission

from directorio.models import User


class EsAdministrador(BasePermission):

    def has_permission(self, request, view):
        return User.objects.get(usuario=request.user).rol == 'administador'


class EsSecretario(BasePermission):

    def has_permission(self, request, view):
        return User.objects.get(usuario=request.user).rol == 'secretario'


class EsPlanificador(BasePermission):

    def has_permission(self, request, view):
        return User.objects.get(usuario=request.user).rol == 'planificador'
