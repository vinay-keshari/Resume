from django import forms
from castapp.models import profile

class registration_form(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField(label='Email', max_length=100)