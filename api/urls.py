from django.urls import path, include
from django.views.generic import TemplateView

from rest_framework import routers

router = routers.DefaultRouter()
from .views import ModuloViewSet, LibroViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'modulos', ModuloViewSet, basename='modulo')
router.register(r'libros', LibroViewSet, basename='libro')

urlpatterns = [
    path('doc/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui'),
] + router.urls
