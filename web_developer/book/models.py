from django.urls import reverse
from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=120)
    author = models.CharField(max_length=150)
    description = models.TextField(default="Описание книги")
    photo = models.ImageField(upload_to="image")
    date_published = models.CharField(max_length=10)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now_add=True)
    comment = models.ForeignKey("Comments", on_delete=models.PROTECT, null=True)
    category = models.ForeignKey("Category", on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name


class Comments(models.Model):
    user = models.IntegerField(db_index=True)
    body = models.TextField(default="Комментарий")
    date_published = models.CharField(max_length=10)

    def __str__(self):
        return self.body


class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category", kwargs={"category_id": self.pk})
