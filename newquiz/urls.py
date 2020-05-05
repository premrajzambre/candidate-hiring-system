from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.urls import path
from . import views

app_name = 'newquiz'


urlpatterns = [
    path('newquiz_home', views.newquiz_home, name='newquiz_home'),
    path('questions/<int:question_id>/', views.question_detail, name='question_detail'),
    path('results/', views.newquiz_results, name='newquiz_results'),
]
