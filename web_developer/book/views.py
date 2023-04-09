from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout, login
from django.contrib.auth.models import User

from .forms import *
from .models import *
from .utils import *


class BookHome(DataMixin, ListView):
    model = Book
    template_name = 'book/book.html'
    context_object_name = 'item'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        more_context = self.get_user_content(title="Главная страница")
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


class SearchBook(DataMixin, LoginView):
    model = Book
    template_name = 'book/book.html'
    context_object_name = 'item'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        if Book.objects.filter(name__icontains=self.request.GET.get('q')):
            context['item'] = Book.objects.filter(name__icontains=self.request.GET.get('q'))
        elif Book.objects.filter(author__icontains=self.request.GET.get('q')):
            context['item'] = Book.objects.filter(author__icontains=self.request.GET.get('q'))
        more_context = self.get_user_content(title="Главная страница")
        return dict(list(context.items()) + list(more_context.items()))


class RegUser(DataMixin, CreateView):
    form_class = RegUserForm
    template_name = 'book/reg.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        more_context = self.get_user_content(title="Регистрация")
        return dict(list(context.items()) + list(more_context.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LogUser(DataMixin, LoginView):
    form_class = LogUserForm
    template_name = 'book/log.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        more_context = self.get_user_content(title="Авторизация")
        return dict(list(context.items()) + list(more_context.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def logOut(request):
    logout(request)
    return redirect('login')


def addComment(request, book_id):
    user = {'user_id': request.user.pk}
    book = {'current_book_id': book_id}

    if request.method == "POST":
        form = AddComment(request.POST)
        if form.is_valid():
            form.cleaned_data.update(user)
            form.cleaned_data.update(book)
            try:
                Comments.objects.create(**form.cleaned_data)
                return redirect(f'/book/{book_id}')
            except:
                form.add_error(None, "Ошибка добавления поста")
    else:
        form = AddComment()

    category = Category.objects.all()
    context = {
        "category": category,
        "form": form
    }

    return render(request, 'book/addComment.html', context=context)


def updateComment(request, book_id, com_id):
    current_user = request.user.pk
    comment_user = Comments.objects.get(pk=com_id).user_id
    book = {'current_book_id': book_id}
    if current_user == comment_user:
        try:
            if request.method == "POST":
                form = UpdateComment(request.POST)
                comment = Comments.objects.get(pk=com_id)
                if form.is_valid():
                    form.cleaned_data.update(book)
                    try:
                        comment.body = form.cleaned_data["body"]
                        comment.save()
                        return redirect(f'/book/{book_id}')
                    except:
                        form.add_error(None, "Ошибка обновления поста")

            else:
                form = UpdateComment()
        except:
            return HttpResponseNotFound("Страница не найдена")
    else:
        return HttpResponseNotFound("Страница не найдена")

    category = Category.objects.all()
    context = {
        "category": category,
        "form": form
    }

    return render(request, 'book/UpdateComment.html', context=context)


def deleteComment(request, book_id, com_id):
    current_user = request.user.pk
    comment_user = Comments.objects.get(pk=com_id).user_id
    if current_user == comment_user:
        try:
            comment = Comments.objects.get(pk=com_id)
            comment.delete()
            return redirect(f'/book/{book_id}')
        except:
            return HttpResponseNotFound("Страница не найдена")
    else:
        return HttpResponseNotFound("Страница не найдена")


def pageNotFound(request, exception):
    return HttpResponseNotFound("Страница не найдена")
