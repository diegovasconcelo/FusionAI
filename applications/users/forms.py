from django import forms
from django.contrib.auth import authenticate
from .models import User

class UserRegisterForm(forms.ModelForm):
    password1 = forms.CharField(
        label = 'Contraseña',
        required = True,
        widget = forms.PasswordInput(
            attrs={
                'class' : 'form-control border-white'
            }
        )
    )
    password2 = forms.CharField(
        label = 'Contraseña (De nuevo)',
        required = True,
        widget = forms.PasswordInput(
            attrs={
                'class' : 'form-control border-white'
            }
        )
    )

    class Meta:
        model = User
        fields = ['email','names','last_name','occupation','gender','date_of_birth']
        
    email = forms.CharField(
        label = 'Email',
        required = True,
        widget=forms.EmailInput(
            attrs={'class': 'form-control border-white'}
        )
    )

    names = forms.CharField(
        label = 'Nombres',
        required = True,
        widget=forms.TextInput(
            attrs={'class': 'form-control border-white'}
        )
    )

    last_name = forms.CharField(
        label = 'Apellidos',
        required = True,
        widget=forms.TextInput(
            attrs={'class': 'form-control border-white'}
        )
    )

    occupation = forms.CharField(
        label = 'Ocupación',
        required = True,
        widget=forms.TextInput(
            attrs={'class': 'form-control border-white'}
        )
    )

    gender = forms.ChoiceField(
        choices = User.GENDER,
        label = 'Género',
        required = True,
        widget=forms.Select(
            attrs={'class': 'form-control border-white'}
        )
    )

    date_of_birth = forms.CharField(
        label = 'Fecha de nacimiento',
        required = True,
        widget=forms.DateInput(
            attrs={'class': 'form-control border-white','type':'date'}
        )
    )


    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        
        if len(password1) < 8:
            self.add_error('password2','La contraseña debe tener al menos 8 caracteres.')
        if password1 != password2:
            self.add_error('password2','Las contraseñas no coinciden.')


class UserLoginForm(forms.Form):
    email = forms.CharField(
        label = 'Correo',
        required = True,
        widget = forms.EmailInput(
            attrs={
                'class': 'form-control border-white'
            }
        )
    )
    password = forms.CharField(
        label = 'Contraseña',
        required = True,
        widget = forms.PasswordInput(
            attrs={
                'class': 'form-control border-white'
            }
        )
    )

    def clean(self):
        cleaned_data = super(UserLoginForm, self).clean()
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        
        if not authenticate(email = email, password = password):
            raise forms.ValidationError('El correo o la contraseña son incorrectos.')

        return self.cleaned_data


class UserPasswordForm(forms.Form):
    password1 = forms.CharField(
        label = 'Contraseña actual',
        required = True,
        widget = forms.PasswordInput(
            attrs={
                'class': 'form-control border-white'
            }
        )
    )

    password2 = forms.CharField(
        label = 'Nueva contraseña',
        required = True,
        widget = forms.PasswordInput(
            attrs = {
                'class': 'form-control border-white'
            }
        )
    )


class UserVerificationForm(forms.Form):
    code = forms.CharField(
        label = 'Código',
        required = True,
        widget = forms.PasswordInput(
            attrs = {
                'class': 'form-control border-white'
            }
        )
    )
    
    def __init__(self, pk, *args, **kwargs):
        self.user_id = pk
        super(UserVerificationForm, self).__init__(*args, **kwargs)

    def clean_code(self):
        verificationCode = self.cleaned_data['code']
        
        if len(verificationCode) == 6:
            active = User.objects.validation_code(self.user_id, verificationCode)
            
            if not active:
                raise forms.ValidationError('Código incorrecto.')    
        else:
            raise forms.ValidationError('Código incorrecto')