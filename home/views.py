
from django.urls import reverse
from django.shortcuts import render

def index(request):
   
    return render(request,'home/index.html')

def gallery(request):
       
    return render(request,'gallery.html')


def contactus(request):
       
    return render(request,'contact-us.html')

def aboutus(request):
       
    return render(request,'about-us.html')







    
   
