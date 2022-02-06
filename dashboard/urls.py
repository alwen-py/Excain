from django.urls import path
from .views import dash
from dashboard import views


urlpatterns = [
    path('dash/',dash, name="dash"),
]
