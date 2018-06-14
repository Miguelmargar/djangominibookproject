from django.conf.urls import url
from django.views.static import serve
from django.conf import settings
from .views import add_book

urlpatterns = [
    url(r"add", add_book, name="add_book"),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]