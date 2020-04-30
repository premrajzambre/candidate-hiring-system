from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

#app_name = 'authenticate'

urlpatterns = [
    path('', views.home, name="home"),
    path('login/',views.login_user, name='login'),
    path('login_success/',views.login_success, name='login_success'),
    path('logout/',views.logout_user, name='logout'),
    path('register/',views.register_user, name='register'),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',views.activate, name='activate'),
    path('edit_profile/',views.edit_profile, name='edit_profile'),
    path('change_password/',views.change_password, name='change_password'),
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name="authenticate/password_reset.html"),name="reset_password"),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name="authenticate/password_reset_sent.html"), name = "password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="authenticate/password_reset_form.html"), name = "password_reset_confirm"),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name="authenticate/password_reset_done.html"), name = "password_reset_complete"),
    path('about', views.about, name='about'),
    #path('quiz/', views.quiz, name='quiz'),
]
