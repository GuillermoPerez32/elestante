from rest_framework import serializers

from api.models import Libro, Material, Modulo
from directorio.serializers import UserModelSerializer


class LibroSerializer(serializers.ModelSerializer):
    usuarios = UserModelSerializer(many=True, read_only=True)

    class Meta:
        model = Libro
        fields = '__all__'


class MaterialSerializer(serializers.ModelSerializer):

    class Meta:
        model = Material
        fields = '__all__'


class ModuloSerializer(serializers.ModelSerializer):
    usuarios = UserModelSerializer(many=True, read_only=True)
    materiales = MaterialSerializer(many=True)

    def create(self, validated_data):
        print(validated_data)
        modulo = Modulo.objects.create(
            categoria=validated_data['categoria'],
        )

        for material in validated_data['materiales']:
            modulo.materiales.create(**material)

        modulo.save()
        return modulo

    class Meta:
        model = Modulo
        fields = '__all__'
        # exclude = ['fecha']
        read_only_fields = ['fecha']