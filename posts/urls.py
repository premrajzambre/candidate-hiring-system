from django.contrib import admin
from django.urls import path, include

from . import views
from posts.views import IndexView, PostListView, PostCreateView, PostDetailView

app_name = "posts"

urlpatterns = [
    # path('', index),
    path('', views.IndexView.as_view(), name='post_home'),
    # path('blog/', post_list, name='post-list'),
    path('blog/', views.PostListView.as_view(), name='blog'),
    path('search/', views.search, name='search'),
    # path('create/', post_create, name='post-create'),
    path('create/', views.PostCreateView.as_view(), name='post-create'),
    # path('post/<id>/', post_detail, name='post-detail'),
    path('post/<pk>/', views.PostDetailView.as_view(), name='post-detail'),
    # path('post/<id>/update/', post_update, name='post-update'),
    #path('tinymce/', include('tinymce.urls')),
]