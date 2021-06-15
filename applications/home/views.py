from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from applications.post.models import Article
from .models import Home
from .forms import SubscriberForm, ContactForm

class HomePage(generic.TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        context["home"] = Home.objects.latest('created')
        context["cover_page"] = Article.objects.cover_page()
        context["articles"] = Article.objects.articles_on_home()
        context["last_articles"] = Article.objects.last_articles_on_home()

        #formSubscriptions
        context["form"] = SubscriberForm
        
        return context
    
    
class SubcriberCreateView(generic.CreateView):
    form_class = SubscriberForm
    success_url = '.'
    
class ContactCreateView(generic.CreateView):
    form_class = ContactForm
    success_url = '.'
