from django.contrib import admin
from .models import Category, Tag, Article

admin.site.register(Category)
admin.site.register(Tag)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('user', 'title','public','cover_page','in_home')
    list_filter = ('user','tag','category','public','cover_page','in_home')
    search_fields = ['title']

admin.site.register(Article, ArticleAdmin)