from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    full_nombre_apellidos = serializers.SerializerMethodField('get_full_nombre_apellidos')

    def get_full_nombre_apellidos(self, obj: Usuario) -> str:
        '''
        Devuelve el nombre completo del usuario
        '''
        return obj.nombre + ' ' + obj.apellidos

    def create(self, validated_data):
        '''
        Crea un usuario
        '''
        if not validated_data.get('nombre'):
            raise serializers.ValidationError('El campo de nombre debe estar configurado')
        usuario = Usuario(
            nombre=validated_data['nombre'],
            apellidos=validated_data['apellidos'],
            email=validated_data['email']
        )
        usuario.set_password(validated_data['password'])
        usuario.save()
        return usuario

    class Meta:
        model = Usuario
        fields = ('id', 'nombre', 'apellidos', 'email', 'full_nombre_apellidos', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }
