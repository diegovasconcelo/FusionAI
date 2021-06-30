from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager

class User(AbstractBaseUser, PermissionsMixin):

    GENDER = [
        ['M', 'Man'],
        ['W', 'Woman'],
        ['N', 'Non binary']
    ]
    
    names = models.CharField(max_length=100, blank=True, verbose_name='names')
    last_name = models.CharField(max_length=100, blank=True, verbose_name='last name')
    occupation = models.CharField(max_length=50, blank=True, verbose_name='occupation')
    email = models.EmailField(unique=True, verbose_name='email')
    date_of_birth = models.DateField(blank=True, verbose_name='date of birth')
    gender = models.CharField(max_length=1, choices=GENDER, blank=True, verbose_name='gender')
    confirm_code = models.CharField(max_length=6, blank=True, verbose_name='confirmation code')
    
    is_staff = models.BooleanField(default=False, verbose_name='staff?')
    is_active = models.BooleanField(default=False, verbose_name='active?')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['names', 'date_of_birth']

    objects = UserManager()

    class Meta:
        verbose_name ='user'
        verbose_name_plural = 'users'

    def __str__(self):
        return self.names + ' ' + self.last_name