from rest_framework import serializers
from django.contrib.auth.models import User
from user.models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['image', 'description', 'nickname']

class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'profile']

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile', {})
        profile = instance.profile

        # Atualiza campos do usuário se fornecidos
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.save()

        # Atualiza campos do perfil
        profile.nickname = profile_data.get('nickname', profile.nickname)
        profile.description = profile_data.get('description', profile.description)
        if self.context['request'].FILES.get('image'):
            profile.image = self.context['request'].FILES['image']
        profile.save()

        return instance
