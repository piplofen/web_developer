from django.urls import path
from django.conf.urls.static import static
#
from web_developer import settings
from .views import *

urlpatterns = [
    path('', main, name='home'),
    path('book/', book),
    path('category/<int:category_id>/', show_category, name='category'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = pageNotFound