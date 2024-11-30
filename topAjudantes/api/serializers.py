from rest_framework import serializers
from topAjudantes import models

class TopAjudantesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TopAjudantes
        fields = '__all__'