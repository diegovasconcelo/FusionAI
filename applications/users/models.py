from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager

class User(AbstractBaseUser, PermissionsMixin):

    GENDER = [
        ['H', 'Hombre'],
        ['M', 'Mujer'],
        ['N', 'No binario'],
        ['O', 'Otro'],
        ['P', 'Prefiero no decir']
    ]
    
    names = models.CharField(max_length=100, blank=True, verbose_name='nombres')
    last_name = models.CharField(max_length=100, blank=True, verbose_name='apellidos')
    occupation = models.CharField(max_length=50, blank=True, verbose_name='ocupación')
    email = models.EmailField(unique=True, verbose_name='correo')
    date_of_birth = models.DateField(blank=True, verbose_name='fecha de nacimiento')
    gender = models.CharField(max_length=1, choices=GENDER, blank=True, verbose_name='Genero')
    confirm_code = models.CharField(max_length=6, blank=True, verbose_name='código de confirmación')
    
    is_staff = models.BooleanField(default=False, verbose_name='¿es staff?')
    is_active = models.BooleanField(default=False, verbose_name='¿es activo?')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['names', 'date_of_birth']

    objects = UserManager()

    class Meta:
        verbose_name ='usuario'
        verbose_name_plural = 'usuarios'

    def __str__(self):
        return self.names + ' ' + self.last_name