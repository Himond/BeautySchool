from django.contrib import admin
from django.urls import path, re_path
from django.contrib import auth
from django.urls import reverse_lazy
from core import views

urlpatterns = [

    path('login/', 'django.contrib.auth.views.login', name='login'),
    path('logout/', 'django.contrib.auth.views.logout', name='logout'),
    path('logout-then-login/', 'django.contrib.auth.views.logout_then_login', name='logout_then_login'),

    path('password-change/', auth.views.PasswordChangeView.as_view(), name='password_change'),
    path('password-change/done/', auth.views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    path('password-reset/', 'django.contrib.auth.views.password_reset', name='password_reset'),
    path('password-reset/done/', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    path('password_reset/confirm/<uidb64>/<token>/', 'django.contrib.auth.views.password_reset_confirm',
        name='password_reset_confirm'),
    path('password-reset/complete/', 'django.contrib.auth.views.password_reset_complete',
         name='password_reset_complete'),


]