from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import SignUpForm, LoginForm, ContactForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import *
from django.contrib import messages
from accounts import forms

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(
                request, 'Your password was successfully updated!')
            return redirect('/')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'home/password_change.html', {
        'form': form
    })

def contact_view(request):
    contactform = ContactForm()
    context = {'contactform': contactform}
    return render(request, 'contact-us.html', context)

def login_view(request):
    form = LoginForm(request.POST or None)
    msg = "Invalid"
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login Successful.')
                return redirect("/")
            else:
                messages.error(request, 'Wrong Username or Password ')
                messages.error(request, form.errors)

        else:
            messages.error(request)
    return render(request, "login.html", {"form": form, "msg": msg})


def register_request(request):
    msg = None
    success = False
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            msg = 'User created successfully.'
            success = True
            return redirect("/login/")
        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()
    return render(request, "registration.html", {"form": form, "msg": msg, "success": success})
