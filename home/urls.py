
from django.urls import path

from home.views import *

urlpatterns = [
    path('',index,name='home'),  
    path('gallery',gallery,name='gallery'),
    path('contactus',contactus,name='conact'),
    path('aboutus',aboutus,name='aboutus')
]
