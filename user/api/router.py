from rest_framework.routers import DefaultRouter
from .viewsets import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)

# Esse `router` será importado no `urls.py` do projeto principal ou em outro lugar.
