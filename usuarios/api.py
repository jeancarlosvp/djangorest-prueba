from rest_framework import viewsets, permissions
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from usuarios.models import Usuario
from usuarios.serializers import UsuarioSerializer

@permission_classes([IsAuthenticated])
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UsuarioSerializer
