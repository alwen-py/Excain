from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import DashBoardLoginForm

def dashboard(request):
    return render(request,'dashboard/admin/dash/basic.html')

def dashlogin(request):
    return render(request,'dashboard/admin/login-2.html')

def users(request):
    return render(request,'dashboard/admin/users.html')

def layouts(request):
    return render(request,'dashboard/admin/forms/layouts.html')


def login_view(request):
    form = DashBoardLoginForm(request.POST or None) 
    msg= "Invalid"
    print("login view")
    if request.method == "POST":
        print("method post")
        if form.is_valid():      
                username = form.cleaned_data.get("username")
                password = form.cleaned_data.get("password")
                user = authenticate(username=username, password=password)
                if request.user.is_superuser: 
                    if user is not None:
                        login(request, user)
                        msg= 'Login successful'
                        return render(request,"dashboard/admin/dash/basic.html",{"form": form, "msg": msg})
                    else:
                        msg = 'Invalid credentials'
                        # return render(request, "dashboard/admin/dash/basic.html", {"form": form, "msg": msg})
        else:
            msg = 'Error validating the form'
            # return render(request, "dashboard/admin/login-2.html", {"form": form, "msg": msg})
    print("last return")  
    return render(request, "dashboard/admin/login-2.html", {"form": form, "msg": msg})

