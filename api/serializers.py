from rest_framework import serializers

from api.models import Libro, Modulo


class LibroSerializer(serializers.ModelSerializer):

    class Meta:
        model = Libro
        fields = '__all__'
        # exclude = ['fecha']
        read_only_fields = ['fecha']

class ModuloSerializer(serializers.ModelSerializer):

    class Meta:
        model = Modulo
        fields = '__all__'
        # exclude = ['fecha']
        read_only_fields = ['fecha']

