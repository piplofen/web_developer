from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm

from .forms import *
from .models import *
from .utils import *


class BookHome(DataMixin, ListView):
    model = Book
    template_name = 'book/book.html'
    context_object_name = 'item'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        more_context = self .get_user_content(title="Главная страница")
        return dict(list(context.items()) + list(more_context.items()))


class BookShow(DataMixin, DetailView):
    model = Book
    template_name = 'book/current_book.html'
    pk_url_kwarg = 'book_id'
    context_object_name = 'item'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        more_context = self.get_user_content(title="Главная страница", category_selected=context["object"].category_id,
                                             comments=Comments.objects.filter(current_book_id=context["object"].pk))
        return dict(list(context.items()) + list(more_context.items()))


class BookCategory(DataMixin, ListView):
    model = Book
    template_name = 'book/book.html'
    context_object_name = 'item'

    def get_queryset(self):
        return Book.objects.filter(category_id=self.kwargs["category_id"])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        more_context = self.get_user_content(title=f"Жанр {str(context['item'][0].category_id)}",
                                             category_selected=context["item"][0].category_id)
        return dict(list(context.items()) + list(more_context.items()))


class RegUser(DataMixin, CreateView):
    form_class = RegUserForm
    template_name = 'book/reg.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        more_context = self.get_user_content(title="Регистрация")
        return dict(list(context.items()) + list(more_context.items()))


class LogUser(DataMixin, LoginView):
    form_class = LogUserForm
    template_name = 'book/log.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        more_context = self.get_user_content(title="Авторизация")
        return dict(list(context.items()) + list(more_context.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def addComment(request, book_id):
    return HttpResponse("Заглушка")


def pageNotFound(request, exception):
    return HttpResponseNotFound("Страница не найдена")