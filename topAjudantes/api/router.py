from rest_framework import routers
from topAjudantes.api import viewsets


topAjudantes_router = routers.DefaultRouter()
topAjudantes_router.register('topAjudantes', viewsets.TopAjudantesViewSet)