# todolist urls
from django.urls import re_path
from todolist import views

urlpatterns = [
    re_path('^$', views.index),
]
