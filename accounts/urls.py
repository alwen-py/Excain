from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView 
from accounts import views
from .views import *
from django.conf.urls import url

urlpatterns = [
    path('login/', login_view, name="login"),
    path('contact-us/', contact_view, name="contact-us"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", views.register_request, name="register"),
    url('change_password',views.change_password, name='change_password'),   
    
]
