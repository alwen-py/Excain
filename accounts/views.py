from audioop import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import SignUpForm, LoginForm
from django.contrib import *
from django.contrib.auth.views import PasswordChangeView,PasswordResetDoneView
from django.urls import reverse_lazy
from django.contrib import messages
class MyPasswordChangeView(PasswordChangeView):
    template_name= 'home/password_change.html'
    def get_success_url(self):
        return reverse('/',name='pswrdchange')
    
class MyPasswordResetDoneView(PasswordResetDoneView):
    template_name='home/password_change_done.html'
     
def login_view(request):
    form = LoginForm(request.POST or None)
    msg = "Invalid"
    if request.method == "POST":
        if form.is_valid():
            print(form)
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
            messages.error(request, 'second else')   
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
    return render(request,"registration.html", {"form": form, "msg": msg, "success": success})