from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=120)
    author = models.CharField(max_length=150)
    photo = models.ImageField(upload_to="image")
    date_published = models.CharField(max_length=10)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
