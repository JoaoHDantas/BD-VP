from rest_framework import serializers
from interaction.models import Interaction

class InteractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interaction
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']