from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label=("Usuario:"), widget=forms.TextInput(attrs={'placeholder': ''}))
    password = forms.CharField(label=("Contraseña:"), widget=forms.PasswordInput(attrs={'placeholder': ''}))