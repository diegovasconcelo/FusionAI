from django.db import models

class FavoriteManager(models.Manager):
    
    def favorite(self, user):
        return self.filter(user=user, article__public = True).order_by('-created')

    def is_favorite(self, user, slug):
        if user.is_anonymous:
            result = False
            favorite_id = False
        else:
            match = self.filter(user=user, article__slug = slug)
            if match.exists():
                result = match
            else:
                result = False
                
        return result

