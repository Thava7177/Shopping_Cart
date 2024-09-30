from django.contrib.auth.forms import UserCreationForm

from django import forms

from .models import User

class CustomUserForm(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter User Name'}))
    email=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Email Address'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Passwoerd'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Re - Enter Password'}))
    class Meta:
        model=User
        fields=[ 'username','email','password1','password2' ]

class Orders(UserCreationForm):
    cname=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    address=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    pinno=forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}))
    mobileno=forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=[ 'cname','address','pinno','mobileno' ]