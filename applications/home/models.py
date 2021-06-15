from django.db import models
# Third_party app
from model_utils.models import TimeStampedModel

class Home(TimeStampedModel):
    title = models.CharField(max_length=70, verbose_name='título')
    description = models.TextField(verbose_name='descripción')
    about_title = models.CharField(max_length=70, verbose_name='titulo sobre nosotros')
    about_text = models.TextField(verbose_name='contenido sobre nosotros')
    contact_email = models.EmailField(blank=True, null=True, verbose_name='correo')
    phone = models.CharField(max_length=20, verbose_name='celular')


    class Meta:
        verbose_name = 'página principal'
        verbose_name_plural ='páginas principales'
    
    def __str__(self):
        return self.title


class Subscriber(TimeStampedModel):
    email = models.EmailField(verbose_name='correo')

    class Meta:
        verbose_name='suscriptor'
        verbose_name_plural='suscriptores'
    
    def __str__(self):
        return self.email


class Contact(TimeStampedModel):
    full_name = models.CharField(max_length=100, verbose_name='Nombre completo')
    email = models.EmailField(verbose_name='correo')
    message = models.TextField(verbose_name='mensaje')

    class Meta:
        verbose_name='contacto'
        verbose_name_plural='contactos'
    
    def __str__(self):
        return self.full_name