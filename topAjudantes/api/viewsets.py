from rest_framework import viewsets, permissions
from topAjudantes import models
from topAjudantes.api import serializers
from .permissions import IsInSpecificGroup
class TopAjudantesViewSet(viewsets.ModelViewSet):
    queryset = models.TopAjudantes.objects.all()
    serializer_class = serializers.TopAjudantesSerializer
    permission_classes = [permissions.IsAuthenticated, IsInSpecificGroup, permissions.DjangoModelPermissions]

    