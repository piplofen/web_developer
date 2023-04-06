from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404

from .models import *

menu = ["Главная", "Поиск", "Войти", "Регистрация"]


def main(request):
    item = Book.objects.all()
    category = Category.objects.all()

    context = {
        "item": item,
        "menu": menu,
        "category": category,
        "title": "Главная страница",
        "category_selected": 0,
    }

    return render(request, 'book/book.html', context=context)


def book(request):
    return render(request, 'book/main.html', {'menu': menu, 'title': "Книга"})


def show_category(request, category_id):
    item = Book.objects.filter(category_id=category_id)
    category = Category.objects.all()

    if len(item) == 0:
        raise Http404()

    context = {
        "item": item,
        "menu": menu,
        "category": category,
        "title": f"Жанр {category_id}",
        "category_selected": category_id,
    }

    return render(request, 'book/book.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound("Страница не найдена")