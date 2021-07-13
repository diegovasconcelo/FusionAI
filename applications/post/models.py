from datetime import timedelta, datetime

from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify
# Third_party app
from model_utils.models import TimeStampedModel
from ckeditor_uploader.fields import RichTextUploadingField

from .managers import PostManager



class Category(TimeStampedModel):
    name = models.CharField(max_length=30, unique=True, verbose_name='name')
    description = models.CharField(max_length=200, unique=True, verbose_name='description')

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class Tag(TimeStampedModel):
    tag = models.CharField(max_length=50, verbose_name='Tag')
    
    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'

    def __str__(self):
        return self.tag

class Article(TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='user')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='category') 
    tag = models.ManyToManyField("post.Tag", verbose_name='tags')
    title = models.CharField(max_length=200, verbose_name='title')
    content = RichTextUploadingField(verbose_name='content')
    public = models.BooleanField(default=False, verbose_name='public?')
    image = models.ImageField(upload_to='entry',verbose_name='image')
    cover_page = models.BooleanField(default=False, verbose_name='cover page?')
    in_home = models.BooleanField(default=False, verbose_name='On the home page?')
    slug = models.SlugField(editable=False, max_length=200)

    objects = PostManager()


    class Meta:
        verbose_name = 'article'
        verbose_name_plural = 'articles'
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        #Generate unic slug
        now = datetime.now()
        total_time = timedelta(hours=now.hour, minutes=now.minute, seconds=now.second)
        seconds = int(total_time.total_seconds())

        slug_unique = '%s %s' % (self.title, str(seconds))
        self.slug = slugify(slug_unique)

        super(Article, self).save(*args, **kwargs)