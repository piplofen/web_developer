from django.urls import path
# from django.conf.urls.static import static

# from web_developer import settings
from .views import *

urlpatterns = [
    path('', main, name='home'),
    path('book/', book)
]

handler404 = pageNotFound