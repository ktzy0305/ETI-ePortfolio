from django import forms
from django.contrib.auth.models import User
import re

class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Username"
            }
        ) 
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Password",
                "type": "password"
            }
        )
    )

class RegistrationForm(forms.Form):
    email = forms.EmailField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "name" : "email",
                "placeholder": "Email",
                "type": "email"
            }
        )
    )

    username = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "name" : "username",
                "placeholder": "Username"
            }
        ) 
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "name" : "password",
                "type": "password",
                "placeholder": "Password"
            }
        )
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "name" : "confirm_password",
                "type": "password",
                "placeholder": "Confirm Password"
            }
        )
    )

    def check_email_exists(self, email):
        return User.objects.filter(email__iexact=email).exists()

    def check_username_exists(self, username):
        return User.objects.filter(username=username).exists()

    def is_email_valid(self, email):
        if re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return True
        else:
            return False

    def is_password_strong(self, password):
        if re.match(r"[A-Za-z0-9@#$%^&+=]{8,}", password):
            return True
        else:
            return False 

    def password_match(self, password, confirm_password):
        if password == confirm_password:
            return True
        else:
            return False
