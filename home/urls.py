from django.urls import path
from home.views import *

urlpatterns = [
    path('',index,name='home'),
    path('gallery',gallery,name='gallery'),
    path('contactus',contactus,name='contactus'),
    path('aboutus',aboutus,name='aboutus') ,
    path('courses',courses,name='courses'), 
    path('single-course/', singlecourse, name='singlecourse'),
    path('single-course/',CourseDetailView.as_view(), name='singlecourse') 
]
