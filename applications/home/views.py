import json
import os

from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy, reverse
from applications.post.models import Article

from .models import Home, Subscriber, Contact
from .forms import SubscriberForm, ContactForm

#email direction
with open("secret.json") as f:
    secret = json.loads(f.read())

def get_secret(secret_name, secrets=secret):
    try:
        return secrets[secret_name]
    except:
        msg = "The variable %s does not exist" % secret_name
        raise ImproperlyConfigured(msg)


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
    
    
class SubcriberCreateView(SuccessMessageMixin, generic.CreateView):

    form_class = SubscriberForm
    success_message = "Thank you for subscribing 😊"
    error_message = "Sorry, something went wrong. Please try again 👀"
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super(SubcriberCreateView, self).get_context_data(**kwargs)

        return context

    def form_valid(self, form):
        subs = Subscriber.objects.get_or_create(
            email = form.cleaned_data['email']
        )
        messages.success(self.request, self.success_message)

         #send email 
        try:
            to_email = form.cleaned_data['email']

            subject = 'Thank you for subscribing'
            message = f'Your subscription has been confirmed. \n\n The FusionAI Team.'
            from_email = get_secret('EMAIL_USER')
            send_mail(subject, message, from_email, [to_email])
        except (RuntimeError, TypeError, NameError):
            pass

        return HttpResponseRedirect(reverse('home_app:index'))
    
    def form_invalid(self, form):
        messages.error(self.request, self.error_message)
        
        return HttpResponseRedirect(reverse('home_app:index'))

    
class ContactCreateView(SuccessMessageMixin, generic.CreateView):
    form_class = ContactForm
    success_message = "Thank you for getting in touch 😊"
    error_message = "Sorry, something went wrong. Please try again 👀"
    template_name = 'includes/contact.html'

    def get_context_data(self, **kwargs):
        context = super(ContactCreateView, self).get_context_data(**kwargs)

        return context
    
    def form_valid(self, form):
        subs = Contact.objects.get_or_create(
            full_name = form.cleaned_data['full_name'],
            email = form.cleaned_data['email'],
            message = form.cleaned_data['message']
        )
        
        messages.success(self.request, self.success_message)
        
        #send email 
        try:
            name = form.cleaned_data['full_name']
            to_email = form.cleaned_data['email']

            subject = 'Thank you for your contact'
            message = f'Hello {name}, thank you for sending your message. We are already working on it. \n\n The FusionAI Team.'
            from_email = get_secret('EMAIL_USER')
            send_mail(subject, message, from_email, [to_email])
        except (RuntimeError, TypeError, NameError):
            pass

        return HttpResponseRedirect(reverse('home_app:index'))

    def form_invalid(self, form):
        messages.error(self.request, self.error_message)
        
        return HttpResponseRedirect(reverse('home_app:index'))