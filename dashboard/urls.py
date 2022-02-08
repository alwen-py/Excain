from django.urls import path

import dashboard
from .views import *
from dashboard import views


urlpatterns = [
    path('dashboard/',dashboard, name="dash"),
    path('dashlogin/', login_view, name="dashlogin"),
    path("users",users, name="users"),
    path("layouts",layouts, name="layouts"),
]
