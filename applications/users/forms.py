from django import forms
from django.contrib.auth import authenticate
from .models import User

class UserRegisterForm(forms.ModelForm):
    password1 = forms.CharField(
        label = 'Contraseña',
        required = True,
        widget = forms.PasswordInput()
    )
    password2 = forms.CharField(
        label = 'Verifique contraseña',
        required = True,
        widget = forms.PasswordInput()
    )

    class Meta:
        model = User
        fields = ['email','names','last_name','gender']

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        
        if len(password1) < 8:
            self.add_error('password2','La contraseña debe tener al menos 8 caracteres')
        if password1 != password2:
            self.add_error('password2','Las contraseñas no coinciden.')


class UserLoginForm(forms.Form):
    email = forms.CharField(
        label = 'Usuario',
        required = True,
        widget = forms.TextInput()
    )
    password = forms.CharField(
        label = 'Contraseña',
        required = True,
        widget = forms.PasswordInput()
    )

    def clean(self):
        cleaned_data = super(UserLoginForm, self).clean()
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        
        if not authenticate(email = email, password = password):
            raise forms.ValidationError('Ups, los datos no son correctos')

        return self.cleaned_data


class UserPasswordForm(forms.Form):
    password1 = forms.CharField(
        label = 'Contraseña actual',
        required = True,
        widget = forms.PasswordInput()
    )

    password2 = forms.CharField(
        label = 'Contraseña nueva',
        required = True,
        widget = forms.PasswordInput()
    )


class UserVerificationForm(forms.Form):
    code = forms.CharField(required = True)
    
    def __init__(self, pk, *args, **kwargs):
        self.user_id = pk
        super(UserVerificationForm, self).__init__(*args, **kwargs)

    def clean_code(self):
        verificationCode = self.cleaned_data['code']
        
        if len(verificationCode) == 6:
            active = User.objects.validation_code(self.user_id, verificationCode)
            
            if not active:
                raise forms.ValidationError('El código no es correcto.')    
        else:
            raise forms.ValidationError('El código no es correcto.')