from django import forms
from django.contrib.auth import authenticate
from .models import User

class UserRegisterForm(forms.ModelForm):
    password1 = forms.CharField(
        label = 'Password',
        required = True,
        widget = forms.PasswordInput(
            attrs={
                'class' : 'form-control border-white'
            }
        )
    )
    password2 = forms.CharField(
        label = 'Password (again)',
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
         label = 'Names',
        required = True,
        widget=forms.TextInput(
            attrs={'class': 'form-control border-white'}
        )
    )

    last_name = forms.CharField(
        label = 'Last name',
        required = True,
        widget=forms.TextInput(
            attrs={'class': 'form-control border-white'}
        )
    )

    occupation = forms.CharField(
        label = 'Occupation',
        required = True,
        widget=forms.TextInput(
            attrs={'class': 'form-control border-white'}
        )
    )

    gender = forms.ChoiceField(
        choices = User.GENDER,
        label = 'Gender',
        required = True,
        widget=forms.Select(
            attrs={'class': 'form-control border-white'}
        )
    )

    date_of_birth = forms.CharField(
        label = 'Date of birth',
        required = True,
        widget=forms.DateInput(
            attrs={'class': 'form-control border-white','type':'date'}
        )
    )


    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        
        if len(password1) < 8:
            self.add_error('password2','The password must be at least 8 characters long.')
        if password1 != password2:
            self.add_error('password2','Passwords do not match.')


class UserLoginForm(forms.Form):
    email = forms.CharField(
        label = 'Email',
        required = True,
        widget = forms.EmailInput(
            attrs={
                'class': 'form-control border-white'
            }
        )
    )
    password = forms.CharField(
        label = 'Password',
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
            raise forms.ValidationError('The email or password you entered is incorrect.')

        return self.cleaned_data


class UserPasswordForm(forms.Form):
    password1 = forms.CharField(
        label = 'Current password',
        required = True,
        widget = forms.PasswordInput(
            attrs={
                'class': 'form-control border-white'
            }
        )
    )

    password2 = forms.CharField(
        label = 'New password',
        required = True,
        widget = forms.PasswordInput(
            attrs = {
                'class': 'form-control border-white'
            }
        )
    )


class UserVerificationForm(forms.Form):
    code = forms.CharField(
        label = 'Code',
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
                raise forms.ValidationError('Incorrect code.')    
        else:
            raise forms.ValidationError('Incorrect code')