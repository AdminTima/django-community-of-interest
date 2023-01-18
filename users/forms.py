from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label="username", widget=forms.TextInput(attrs={"class": "form_inp", "placeholder": "Enter username"}))
    password1 = forms.CharField(label="password", widget=forms.PasswordInput(attrs={"class": "form_inp", "placeholder": "Enter password"}))
    password2 = forms.CharField(label="password confirm", widget=forms.PasswordInput(attrs={"class": "form_inp", "placeholder": "Confirm password"}))

    class Meta:
        model = User
        fields = ("username", "password1", "password2")


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label="username", widget=forms.TextInput(attrs={"class": "form_inp", "placeholder": "Enter username"}))
    password = forms.CharField(label="password", widget=forms.PasswordInput(attrs={"class": "form_inp", "placeholder": "Enter password"}))


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("bio", "photo")


class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username",)
