from django.contrib import admin
from django.urls import path, include
# from django.conf.urls.static import static
#
from book.views import main
# from web_developer import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('book.urls'))
]
#
# if settings.DEBUG:
#         urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
