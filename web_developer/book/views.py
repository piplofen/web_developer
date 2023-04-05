from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

from .models import *

menu = ["О сайте", "Войти", "Регистрация"]


def main(request):
    item = Book.objects.all()
    return render(request, 'book/book.html', {"item": item, 'menu': menu, 'title': "Главная страница"})


def book(request):
    return render(request, 'book/main.html', {'menu': menu, 'title': "Книга"})


def pageNotFound(request, exception):
    return HttpResponseNotFound("Страница не найдена")