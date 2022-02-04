from django import template
from django.template import loader
from django.urls import reverse
from django.shortcuts import render

def index(request):
   
    return render(request,'home/index.html')




    
   
