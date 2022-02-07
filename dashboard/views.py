
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm
# Create your views here.

def dash(request):
    return render(request,'dashboard/admin/dash/basic.html')


def dashlogin(request):
    return render(request,'dashboard/admin/login-2.html')


def login_view(request):
    form = LoginForm(request.POST or None)

    
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
                return render(request, "dashboard/admin/dash/basic.html", {"form": form, "msg": msg})
        else:
            return render(request, "dashboard/admin/login-2.html", {"form": form, "msg": msg})
    return render(request, "dashboard/admin/login-2.html", {"form": form, "msg": msg})

