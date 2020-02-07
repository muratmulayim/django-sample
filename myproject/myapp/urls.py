

from django.conf.urls import include, url
from django.contrib import admin
from myapp.views import Second

urlpatterns = [
    url(r'^first/$', 'myapp.views.first'),
    url(r'^second/$', Second.as_view()),
    url(r'^name/$', 'myapp.views.get_name'),
    url(r'^error/$', 'myapp.views.error_page'),
]
