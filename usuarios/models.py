from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from usuarios.managers import UsuarioManager

class Usuario(AbstractBaseUser):
    '''
    Modelo de usuario personalizado 
    '''
    nombre = models.CharField(max_length=100, blank=True, null=True)
    apellidos = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre']

    objects = UsuarioManager()

    def __str__(self):
        return self.email
    