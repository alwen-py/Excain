from django.urls import path
from home.views import *
from django.conf.urls import url


urlpatterns = [
    path('',index,name='home'),
    path('gallery',gallery,name='gallery'),
    path('contact-us',contactus,name='contactus'),
    path('aboutus',aboutus,name='aboutus') ,
    path('courses/',courses,name='courses'), 
    path('course-detail/<int:id>',coursedetail)
]
