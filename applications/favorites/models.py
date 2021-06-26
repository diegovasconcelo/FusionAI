from django.db import models
from django.conf import settings
from applications.post.models import Article
from .managers import FavoriteManager
# Third_party app
from model_utils.models import TimeStampedModel

class Favorite(TimeStampedModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='user_favorites',
        on_delete=models.CASCADE,
        verbose_name='usuario'
    )
    article = models.ForeignKey(
        Article,
        related_name='article_favorites',
        on_delete=models.CASCADE,
        verbose_name='entrada'
    )

    objects = FavoriteManager()

    class Meta:
        unique_together = ['user', 'article']
        verbose_name = 'favorito'
        verbose_name_plural = 'favoritos'

    def __str__(self):
        return str(self.id) + ' ' +self.article.title