from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings

from . import views

app_name = 'quiz'


urlpatterns = [
    url(r'^quiz_start', views.quiz_start, name = 'quiz_start'),
    url(r'^start', views.start, name = 'start'),
    url(r'^quiz_home', views.quiz_home, name = 'quiz_home'),
    url(r'^result', views.result, name = 'result'),
    url(r'^instructions', views.instructions, name = 'instructions'),
    url(r'^contact', views.contact, name = 'contact'),
    url(r'^(?P<choice>[\w]+)', views.questions, name = 'questions'),
]
