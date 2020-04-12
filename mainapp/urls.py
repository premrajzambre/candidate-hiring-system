from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'mainapp'

urlpatterns = [
    path('upload', views.upload, name = 'upload'),
    path('dashboard', views.dashboard, name = 'dashboard'),
    path('history', views.history, name = 'history'),
    path('hr_admin', views.hr_admin, name = 'hr_admin'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
