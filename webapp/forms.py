from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms 
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput , TextInput

#  - Register a user / Create a user
 
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']

        
# - LOgin a user

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

# 2:00:42 /