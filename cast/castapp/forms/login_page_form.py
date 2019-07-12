from django import forms
from castapp.models import profile

class login_page_form(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username'}) ,label='', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}), label='')