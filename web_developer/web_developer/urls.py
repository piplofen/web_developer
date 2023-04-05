from django.contrib import admin
from django.urls import path, include

from book.views import main

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('book.urls'))
]
