from django.db import models
# Third_party app
from model_utils.models import TimeStampedModel

class Home(TimeStampedModel):
    title = models.CharField(max_length=70, verbose_name='title')
    description = models.TextField(verbose_name='description')
    about_title = models.CharField(max_length=70, verbose_name='about title')
    about_text = models.TextField(verbose_name='about description')
    contact_email = models.EmailField(blank=True, null=True, verbose_name='email')
    subject_email = models.CharField(max_length=50, blank=True, null=True, verbose_name='email subject')
    body_email = models.CharField(max_length=100, blank=True, null=True, verbose_name='email body')
    web = models.CharField(max_length=50, blank=True, null=True, verbose_name='web')
    repository = models.CharField(max_length=100, blank=True, null=True, verbose_name='repository')
    phone = models.CharField(blank=True, null=True, max_length=20, verbose_name='phone')


    class Meta:
        verbose_name = 'homepage'
        verbose_name_plural ='main pages'
    
    def __str__(self):
        return self.title


class Subscriber(TimeStampedModel):
    email = models.EmailField(verbose_name='email')

    class Meta:
        verbose_name='subscriber'
        verbose_name_plural='subscribers'
    
    def __str__(self):
        return self.email


class Contact(TimeStampedModel):
    full_name = models.CharField(max_length=100, verbose_name='name')
    email = models.EmailField(verbose_name='email')
    message = models.TextField(verbose_name='message')

    class Meta:
        verbose_name='contact'
        verbose_name_plural='contacts'
    
    def __str__(self):
        return self.full_name