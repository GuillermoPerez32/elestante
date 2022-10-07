from rest_framework.routers import DefaultRouter
from .views import ModuloViewSet, LibroViewSet
from django.urls import path, include

from rest_framework import routers

router = routers.DefaultRouter()

router = DefaultRouter()
router.register(r'modulos', ModuloViewSet, basename='modulo')
router.register(r'libros', LibroViewSet, basename='libro')

urlpatterns = [
] + router.urls
