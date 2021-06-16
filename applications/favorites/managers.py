from django.db import models

class FavoriteManager(models.Manager):
    
    def favorite(self, user):
        return self.filter(user=user, article__public = True).order_by('-created')

