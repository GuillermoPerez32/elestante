from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.request import Request

from directorio.models import User


class EsAdministrador(BasePermission):

    def has_permission(self, request: Request, view):

        if request.user.is_authenticated:
            return request.user.rol == 'administrador'
        return False


class EsSecretario(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.user.rol == 'secretario'
        return False


class ReadOnly(BasePermission):

    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS
        )


class EsPlanificador(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.user.rol == 'planificador'
        return False
