from django.urls import path
import dashboard
from .views import *
from dashboard import views
from django.conf.urls import url


urlpatterns = [
    path('dashboard/',dashboard, name="dash"),
    path('dashlogin/', login_view, name="dashlogin"),
    path("users",UserListView.as_view(), name="users"),
    path("layouts",layouts, name="layouts"),
    url('change-dash-password',views.change_password, name='change_password'),   

]
