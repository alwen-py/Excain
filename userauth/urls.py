
from django.contrib import admin
from django.urls import path,include

from userauth.views import sign

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',sign,name='userauth'),
]
