from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .forms import ApplicationForm
from django.views.generic import TemplateView
from rest_framework import routers
from .views import get_data, hr_admin_View, ChartView, StatisticsView

app_name = 'mainapp'

router = routers.DefaultRouter()
#router.register('mainapp', views.salary)
urlpatterns = [
    path('upload', views.upload, name = 'upload'),
    path('dashboard', views.dashboard, name = 'dashboard'),
    path('past', views.history, name = 'past'),
    path('hr_admin', hr_admin_View.as_view(), name = 'hr_admin'),
    path('api/data/',get_data,name='api-data'),
    path('api/chart/data/',ChartView.as_view(),name='chart-data'),
    path('application',views.application, name = 'application'),
    path('salary', views.salary, name = 'salary'),
    path('api/', include(router.urls)),
    #path('status/', views.salary),
    path('new_process', views.new_process, name = 'new_process'),
    path('invitation', views.invitation, name = 'invitation'),
    path('statistics', StatisticsView.as_view(), name = 'statistics'),
    path('temp', views.temp, name = 'temp'),
    path('abouta', views.abouta, name = 'abouta'),
    path('interview', views.interview, name = 'interview'),
    path('update_candidate/<str:pk>', views.update_candidate, name='update_candidate'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
