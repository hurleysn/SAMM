from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm): #all same properties as user creation form
    first_name= forms.CharField(max_length=50)
    last_name= forms.CharField(max_length=50)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["first_name","last_name","username", "email", "password1", "password2"]
