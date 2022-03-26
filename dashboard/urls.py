from django.urls import path
from dashboard import forms
from excain.settings import ADMIN_LOGIN_URL
from .views import *
from django.conf.urls import url


urlpatterns = [
    path('login/', login_view, name="admin-login"),
    path('', login_required(dashboard, login_url=ADMIN_LOGIN_URL)),
    path("users/", login_required(UserListView.as_view(), login_url=ADMIN_LOGIN_URL), name="users"),
    path("form/", login_required(form, login_url=ADMIN_LOGIN_URL)),
    path("layouts/", login_required(layouts, login_url=ADMIN_LOGIN_URL), name="layouts"),
    url('change-password/', login_required(change_password, login_url=ADMIN_LOGIN_URL),)
]
