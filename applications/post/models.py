from django.db import models
from django.conf import settings
# Third_party app
from model_utils.models import TimeStampedModel
from ckeditor_uploader.fields import RichTextUploadingField

from .managers import PostManager



class Category(TimeStampedModel):
    name = models.CharField(max_length=30, unique=True, verbose_name='nombre')
    description = models.CharField(max_length=200, unique=True, verbose_name='descripcion')

    class Meta:
        verbose_name = 'categoría'
        verbose_name_plural = 'categorías'

    def __str__(self):
        return self.name

class Tag(TimeStampedModel):
    tag = models.CharField(max_length=30, verbose_name='Tag')
    
    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'

    def __str__(self):
        return self.tag

class Article(TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='usuario')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='categoría') 
    tag = models.ManyToManyField("post.Tag", verbose_name='tags')
    title = models.CharField(max_length=200, verbose_name='título')
    content = RichTextUploadingField(verbose_name='contenido')
    public = models.BooleanField(default=False, verbose_name='¿publicado?')
    image = models.ImageField(upload_to='entry',verbose_name='imagen')
    cover_page = models.BooleanField(default=False, verbose_name='¿en portada?')
    in_home = models.BooleanField(default=False, verbose_name='¿en patalla principal?')
    slug = models.SlugField(editable=False, max_length=200)

    objects = PostManager()


    class Meta:
        verbose_name = 'artículo'
        verbose_name_plural = 'artículos'
    
    def __str__(self):
        return self.title