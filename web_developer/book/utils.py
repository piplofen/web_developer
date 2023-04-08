from .models import *

menu = ["Главная", "Поиск", "Войти", "Регистрация"]


class DataMixin:
    def get_user_content(self, **kwargs):
        context = kwargs
        category = Category.objects.all()
        context['menu'] = menu
        context['category'] = category
        if 'category_selected' not in context:
            context['category_selected'] = 0
        return context