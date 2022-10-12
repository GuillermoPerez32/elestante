from rest_framework import serializers

from api.models import Libro, Material, Modulo
from directorio.serializers import UserModelSerializer


class LibroSerializer(serializers.ModelSerializer):
    usuarios = UserModelSerializer(many=True, read_only=True)

    class Meta:
        model = Libro
        fields = '__all__'
        # exclude = ['fecha']
        read_only_fields = ['fecha']


class MaterialSerializer(serializers.ModelSerializer):

    class Meta:
        model = Material
        fields = '__all__'


class ModuloSerializer(serializers.ModelSerializer):
    usuario = UserModelSerializer()
    materiales = MaterialSerializer(many=True)

    class Meta:
        model = Modulo
        fields = '__all__'
        # exclude = ['fecha']
        read_only_fields = ['fecha']
