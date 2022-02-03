from django.shortcuts import render
from django import template
from django.template import loader
from django.urls import reverse

def sign(request):
   
    return render(request,'authenticate.html')


    
   

# Create your views here.
