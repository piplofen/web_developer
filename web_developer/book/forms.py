from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm


class AddComment(forms.Form):
    b = Book.objects.all()
    body = forms.CharField(widget=forms.Textarea(attrs={"cols": 60, "rows": 10}), label="Текст комментария")
    # current_book = forms.CharField(widget=forms.MultipleHiddenInput, )
    # current_book = forms.ModelChoiceField(queryset=b.pk)


# class RegUser(UserCreationForm):
#     class Meta:
#         pass