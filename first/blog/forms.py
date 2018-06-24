from django import forms
from django.contrib.auth.forms import UserCreationForm

class commentform(forms.Form):
    name=forms.CharField(max_length=20)
    message=forms.CharField(max_length=300)
    belongto=forms.CharField(widget=forms.HiddenInput(),max_length=300)