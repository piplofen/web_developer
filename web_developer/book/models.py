from django.urls import reverse
from django.db import models
# from django.contrib.auth.models import AbstractUser, UserManager
from django.contrib.auth import get_user_model
from web_developer import settings


class Book(models.Model):
    name = models.CharField(max_length=120)
    author = models.CharField(max_length=150)
    description = models.TextField(default="Описание книги")
    photo = models.ImageField(upload_to="image", blank=True)
    date_published = models.CharField(max_length=10)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now_add=True)
    # comment = models.ForeignKey("Comments", on_delete=models.PROTECT, null=True)
    category = models.ForeignKey("Category", on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("item", kwargs={"item_id": self.pk})

    class Meta:
        verbose_name = "Книги"
        verbose_name_plural = "Книги"


class Comments(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.PROTECT, null=True)
    current_book = models.ForeignKey("Book", on_delete=models.PROTECT, null=True)
    body = models.TextField(verbose_name="Комментарий")
    date_published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body

    def get_absolute_url(self):
        return reverse("comments", kwargs={"comments_id": self.pk})

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"


class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category", kwargs={"category_id": self.pk})

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
