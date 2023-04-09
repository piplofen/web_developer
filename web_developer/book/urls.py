from django.urls import path
from django.conf.urls.static import static

from web_developer import settings
from .views import *

urlpatterns = [
    path('', BookHome.as_view(), name='home'),
    path('book/<int:book_id>/', BookShow.as_view(), name='book'),
    path('category/<int:category_id>/', BookCategory.as_view(), name='category'),
    path('login/', LogUser.as_view(), name="login"),
    path('reg/', RegUser.as_view(), name="reg"),
    path('add_comment/<int:book_id>/', addComment, name='add'),
    path('delete_comment/<int:book_id>/<int:com_id>', deleteComment, name='delete'),
    path('update_comment/<int:book_id>/<int:com_id>', updateComment, name='update'),
    path('logout', logOut, name='logout'),
    path('search/', SearchBook.as_view(), name='search')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = pageNotFound
