from django.conf.urls import url,include
from django.contrib import admin
from . import views

app_name = 'quiz'

urlpatterns = [
    url(r'^quiz_home', views.quiz_home, name = 'quiz_home'),
    url(r'^result', views.result, name = 'result'),
    url(r'^instructions', views.instructions, name = 'instructions'),
    url(r'^(?P<choice>[\w]+)', views.questions, name = 'questions'),
]
