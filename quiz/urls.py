from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings

from . import views

app_name = 'quiz'


urlpatterns = [
    url(r'^$', views.quiz_home, name = 'quiz_home'),
    url(r'^result', views.result, name = 'result'),
    url(r'^instructions', views.instructions, name = 'instructions'),
    url(r'^contact', views.contact, name = 'contact'),
    url(r'^(?P<choice>[\w]+)', views.questions, name = 'questions'),
]
