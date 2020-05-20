from django.contrib import admin

from .models import Author, Post, PostView

admin.site.register(Author)
# site.register(Category)
admin.site.register(Post)
admin.site.register(PostView)
