from django.urls import path

from .views import *

urlpatterns = [
    path('', main, name='home'),
    path('book/', book)
]

handler404 = pageNotFound
