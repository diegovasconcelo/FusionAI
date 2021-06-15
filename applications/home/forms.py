from django import forms
from .models import Subscriber, Contact

class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = [
            'email',
        ]
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'placeholder':'email',
                    'class': 'form-control'
                }     
            )   
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('__all__')