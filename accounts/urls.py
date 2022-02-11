from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView 
from accounts import views
from .views import register_request

urlpatterns = [
    path('login/', login_view, name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", views.register_request, name="register"),
    path('change-password/',MyPasswordChangeView.as_view(),name='password-change-view'),
     path('change-password/done',MyPasswordResetDoneView.as_view(),name='password-change-view')
    
]
