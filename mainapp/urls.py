from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .forms import ApplicationForm

app_name = 'mainapp'

urlpatterns = [
    path('upload', views.upload, name = 'upload'),
    path('dashboard', views.dashboard, name = 'dashboard'),
    path('history', views.history, name = 'history'),
    path('hr_admin', views.hr_admin, name = 'hr_admin'),
    path('application',views.application, name = 'application'),
    path('can_pass', views.can_pass, name = 'can_pass'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
