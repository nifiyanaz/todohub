from django import forms
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from .models import Tasks

# class TaskForm(forms.Form):
#     task=forms.CharField(max_length=100)
#     priority=forms.IntegerField(min_value=1,max_value=10)
#     dedline=forms.DateField()

class TaskForm(forms.ModelForm):
    class Meta:
        model=Tasks
        fields=['title']

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'username'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'password'}))

class SignupForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password','password2']
