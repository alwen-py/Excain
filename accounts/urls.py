

from cgitb import html
from re import template
from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView 
from accounts import views
from .views import register_request

urlpatterns = [
    path('login/', login_view, name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", views.register_request, name="register"),
    path("changepassword/",auth_views.PasswordChangeView.as_view(template_name='home/password_change.html'),name="password_change")
]
