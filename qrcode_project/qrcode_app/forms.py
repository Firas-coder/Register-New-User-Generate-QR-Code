# forms.py
from django import forms
from .models import UserQRCode
from django import forms
#import library to create new user (register)
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#import library to create new user (register)

class QRUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

