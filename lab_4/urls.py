from django.urls import re_path
from django.conf.urls import url
from .views import index
#url for app
urlpatterns = [
    re_path(r'^$', index, name='chat'),
]
