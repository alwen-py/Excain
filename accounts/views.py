# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Create your views here.
import email
from django.urls import reverse
from django import template
from django.contrib import messages

from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import SignUpForm, LoginForm
from django.http import HttpResponse, HttpResponseRedirect


def login_view(request):
    form = LoginForm(request.POST or None)

    msg1 = "None"
    msg= "Invalid"

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                return render(request, "login.html", {"form": form, "msg": msg})
        else:
            return render(request, "login.html", {"form": form, "msg": msg})
    return render(request, "login.html", {"form": form, "msg": msg})


def register_request(request):
    
    msg = None
    if request.method == "POST":
        form = SignUpForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'User created successfully.'
            
            success = True

            # return redirect("/login/")

        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()
    return render(request,"registration.html",{"form": form, "msg": msg})


# def register_user(request):
#     msg = None
#     success = False

#     if request.method == "POST":
#         form = NewUserForm(request.POST)

#         if form.is_valid():
#             print(form)
#             form.save()
#             username = form.cleaned_data.get("username")
#             email = form.cleaned_data.get("email")
#             raw_password = form.cleaned_data.get("password1")
#             user = authenticate(username=username, password=raw_password)
#             user.email = email
#             user.save()
#             msg = 'User created successfully.'

#             success = True

#             return render(request=request, template_name='authentication.html')

#         else:
#             msg = 'Form is not valid'
#     else:
#         form = NewUserForm()

#     return render(request, "authentication.html", {"form": form, "msg": msg, "success": success})


# def pages(request):
#     context = {}
#     # All resource paths end in .html.
#     # Pick out the html file name from the url. And load that template.
#     try:

#         load_template = request.path.split('/')[-1]

#         if load_template == 'admin':
#             return HttpResponseRedirect(reverse('admin:index'))
#         context['segment'] = load_template

#         html_template = loader.get_template('home/' + load_template)
#         return HttpResponse(html_template.render(context, request))

#     except template.TemplateDoesNotExist:

#         html_template = loader.get_template('home/page-404.html')
#         return HttpResponse(html_template.render(context, request))

#     except:
#         html_template = loader.get_template('home/page-500.html')
#         return HttpResponse(html_template.render(context, request))
