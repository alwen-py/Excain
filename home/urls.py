from django.urls import path
from home.views import *

urlpatterns = [
    path('',index,name='home'),
    path('gallery/',gallery,name='gallery'),
    path('contact-us/',contactUs,name='contactus'),
    path('courses/',courses,name='contactus'),
    path('about-us/',aboutUs,name='aboutus'),
    path('course-detail/<int:id>/', courseDetail, name='courseDetail')
]
