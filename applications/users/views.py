import json
import os

from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views import generic

from .forms import UserRegisterForm, UserLoginForm, UserPasswordForm, UserVerificationForm
from .models import User
from .functions import code_generator

#email direction
with open("secret.json") as f:
    secret = json.loads(f.read())

def get_secret(secret_name, secrets=secret):
    try:
        return secrets[secret_name]
    except:
        msg = "The variable %s does not exist" % secret_name
        raise ImproperlyConfigured(msg)


class UserRegister(generic.FormView):
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('home_app:index')

    def form_valid(self, form):
        
        # generated code for registration
        code = code_generator()

        user = User.objects.create_user(
            email = form.cleaned_data['email'],
            names = form.cleaned_data['names'],
            last_name = form.cleaned_data['last_name'],
            occupation = form.cleaned_data['occupation'],
            gender = form.cleaned_data['gender'],
            date_of_birth = form.cleaned_data['date_of_birth'],
            password = form.cleaned_data['password1'],
            confirm_code = code
        )

        #send code by email
        subject = 'Confirmation code'
        message = f'Hello, the code is: {code}'
        from_email = get_secret('EMAIL_USER')
        send_mail(subject, message, from_email,[form.cleaned_data['email']])

        return HttpResponseRedirect(
            reverse(
                'users_app:userVerification',
                kwargs = {'pk': user.id}
            )
        )    


class UserLogin(generic.FormView):
    template_name = 'users/login.html'
    form_class = UserLoginForm
    success_url = reverse_lazy('favorites_app:favoriteItems')

    def form_valid(self, form):
        user = authenticate(
            email=form.cleaned_data['email'],
            password = form.cleaned_data['password']
        )

        login(self.request, user)

        return super(UserLogin, self).form_valid(form)


class UserLogout(generic.View):

    def get(self, request, *args, **kwargs):
        logout(request)
        
        return HttpResponseRedirect(reverse('users_app:userLogin'))    


class UserPasswordUpdate(LoginRequiredMixin, generic.FormView):
    template_name = 'users/password-update.html'
    form_class = UserPasswordForm
    success_url = reverse_lazy('users_app:userLogin')
   
    # LoginRequired
    login_url = reverse_lazy('users_app:userLogin')

    def form_valid(self, form):
        userAuth = self.request.user
        user = authenticate(
            username = userAuth.username,
            password = form.cleaned_data['password1']
        )

        if user:
            newPassword = form.cleaned_data['password2']
            userAuth.set_password(newPassword)
            userAuth.save()

        logout(self.request)

        return super(UserPasswordUpdate, self).form_valid(form)


class UserVerification(generic.FormView):
    template_name = 'users/verification.html'
    form_class = UserVerificationForm
    success_url = reverse_lazy('users_app:userLogin')

    def get_form_kwargs(self):
        # Return the keyword arguments for instantiating the form.
        kwargs = super(UserVerification, self).get_form_kwargs()
        kwargs.update({
            'pk': self.kwargs['pk']
        })

        return kwargs

    def form_valid(self, form):
        User.objects.filter(id = self.kwargs['pk']).update(is_active=True)
        return super(UserVerification, self).form_valid(form)