from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from applications.post.models import Article

class HomePage(generic.TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        context["cover_page"] = Article.objects.cover_page()
        context["articles"] = Article.objects.articles_on_home()
        context["last_articles"] = Article.objects.last_articles_on_home()
        
        return context
    
