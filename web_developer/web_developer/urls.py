from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
#
from book.views import *
from web_developer import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('book.urls'))
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#
# if settings.DEBUG:
#         urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
