from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, User, AuthenticationForm
from django.views.generic import CreateView


class RegUserForm(UserCreationForm):
    username = forms.CharField(label="Имя пользователя", widget=forms.TextInput(attrs={"class": "form-input"}))
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={"class": "form-input"}))
    password2 = forms.CharField(label="Повтор пароля", widget=forms.PasswordInput(attrs={"class": "form-input"}))

    class Meta:
        model = User
        fields = ("username", "password1", "password2")


class LogUserForm(AuthenticationForm):
    username = forms.CharField(label="Имя пользователя", widget=forms.TextInput(attrs={"class": "form-input"}))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={"class": "form-input"}))


class AddComment(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ("body",)
        widgets = {
            "body": forms.Textarea(attrs={"class": "form-input"})
        }


class UpdateComment(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ("body",)
        widgets = {
            "body": forms.Textarea(attrs={"class": "form-input"})
        }
