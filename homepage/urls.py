from django.urls import re_path
from django.conf.urls import url
from .views import index, about, portofolio
from .views import guest_form, message_post, message_table 
#url for app
urlpatterns = [
    re_path(r'^$', index, name='index'),
    re_path(r'^about', about, name='about'),
    re_path(r'^portofolio', portofolio, name='portofolio'),

    re_path(r'^guest_form', guest_form, name='guest_form'),
    url(r'^add_message', message_post, name='add_message'),
    url(r'^result_table', message_table, name='result_table'),
]
