from django.db import models

class PostManager(models.Manager):

    def cover_page(self):
        return self.filter(public=True, cover_page=True).order_by('-created').first()
    
    def articles_on_home(self):
        return self.filter(public=True, in_home=True).order_by('-created')[:4]

    def last_articles_on_home(self):
        return self.filter(public=True).order_by('-created')[:6]