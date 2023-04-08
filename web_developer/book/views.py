from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.views.generic import ListView, DetailView

from .forms import *
from .models import *

menu = ["Главная", "Поиск", "Войти", "Регистрация"]


class BookHome(ListView):
    model = Book
    template_name = 'book/book.html'
    context_object_name = 'item'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = Category.objects.all()
        context["title"] = "Главная страница"
        context["category_selected"] = 0
        return context


class BookShow(DetailView):
    model = Book
    template_name = 'book/current_book.html'
    pk_url_kwarg = 'book_id'
    context_object_name = 'item'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = Category.objects.all()
        context["title"] = "Главная страница"
        context["category_selected"] = context["object"].category_id
        context["comments"] = Comments.objects.filter(current_book_id=context["object"].pk)
        return context


def addComment(request, book_id):
    item = Book.objects.get(pk=book_id)
    category = Category.objects.all()

    if request.method == "POST":
        form = AddComment(request.POST)
        if form.is_valid():
            try:
                comment = Comments()
                comment.current_book_id = item.pk
                comment.user_id= 2
                comment.body = request.POST.get("body")
                comment.save()
                return redirect("home")
            except:
                form.add_error(None, "Ошибка добавления комментария")
    else:
        form = AddComment()

    context = {
        "item": item,
        "menu": menu,
        "category": category,
        "title": "Добавление комментария",
        "category_selected": 0,
        "form": form
    }

    return render(request, 'book/addComment.html', context=context)


def login(request):
    return HttpResponse("Авторизация")


def reg(request):
    return HttpResponse("Регистрация")


class BookCategory(ListView):
    model = Book
    template_name = 'book/book.html'
    context_object_name = 'item'

    def get_queryset(self):
        return Book.objects.filter(category_id=self.kwargs["category_id"])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = Category.objects.all()
        context["title"] = f"Жанр {str(context['item'][0].category_id)}"
        context["category_selected"] = context["item"][0].category_id
        return context


def RegUser(request):
    form = UserCreationForm

    context = {
        "menu": menu,
        "title": "Главная страница",
        "category_selected": 0,
    }

    return render(request, 'book/reg.html', context=context)


def addComment(request, book_id):
    item = Book.objects.get(pk=book_id)
    category = Category.objects.all()

    if request.method == "POST":
        form = AddComment(request.POST)
        if form.is_valid():
            try:
                comment = Comments()
                comment.current_book_id = item.pk
                comment.user_id= 2
                comment.body = request.POST.get("body")
                comment.save()
                return redirect("home")
            except:
                form.add_error(None, "Ошибка добавления комментария")
    else:
        form = AddComment()

    context = {
        "item": item,
        "menu": menu,
        "category": category,
        "title": "Добавление комментария",
        "category_selected": 0,
        "form": form
    }

    return render(request, 'book/addComment.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound("Страница не найдена")