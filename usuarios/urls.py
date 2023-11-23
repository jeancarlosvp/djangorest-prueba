from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from usuarios.api import UsuarioViewSet

routers = routers.DefaultRouter()
routers.register('api/usuarios', UsuarioViewSet)

urlpatterns = routers.urls

urlpatterns += [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]
