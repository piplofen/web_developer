from django.contrib import admin

from .models import *


class BookAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "author", "date_published", "time_create", "photo")
    list_display_links = ("id", "name")
    search_fields = ("title", "author", "date_published")
    ordering = ["id"]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")
    search_fields = ("name",)
    ordering = ["id"]


class CommentsAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "body", "date_published")
    list_display_links = ("id", "user")
    search_fields = ("user",)
    ordering = ["id"]


admin.site.register(Book, BookAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comments, CommentsAdmin)
