from . import views
from django.contrib import admin
from django.conf import settings
from django.urls import path, include

app_name = 'career'

urlpatterns = [
    path('blog', views.blog, name = 'blog'),
    path('aboutc', views.aboutc, name = 'aboutc'),
]
