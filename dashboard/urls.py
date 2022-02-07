from django.urls import path
from .views import *
from dashboard import views


urlpatterns = [
    path('dash',dash, name="dash"),
    path('dashlogin/', login_view, name="dashlogin")
    
]
