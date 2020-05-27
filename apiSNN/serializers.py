from rest_framework import serializers
from apiSNN import models

class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'description',
        )
        model = models.Libro

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'pclass',
            'sex',
            'age',
            'fare',
            'embarked',
            'survived',
        )
        model = models.Persona

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'image',
            'label',
            'probability',
        )
        model = models.Image