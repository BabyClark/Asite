from django import forms
from django.contrib.auth.forms import UserCreationForm
class MyUser(forms.Form):
    user=forms.CharField(label='your name',max_length=5)
    passw1 = forms.CharField(label='password', widget=forms.PasswordInput)
    passw2 = forms.CharField(label='password confirm',widget=forms.PasswordInput)
    email=forms.EmailField(label='email',widget=forms.EmailInput)

class Login(forms.Form):
    username=forms.CharField(label='用户名',max_length=8)
    password=forms.CharField(label='密码',max_length=20,widget=forms.PasswordInput)

class user_message(forms.Form):
    username =forms.CharField(max_length=20)
    des = forms.CharField(max_length=50)
    email = forms.EmailField()
    school = forms.CharField(max_length=30)
    subject = forms.CharField(max_length=30)

class user_email(forms.Form):
    email=forms.EmailField(max_length=30)
    content=forms.CharField(max_length=300)

class message(forms.Form):
    name=forms.CharField()
    email=forms.CharField()
    phone=forms.CharField()
    messages=forms.CharField()

class uploadfile(forms.Form):
    name=forms.CharField(max_length=20)
    subject=forms.CharField(max_length=200)
    file=forms.FileField()
