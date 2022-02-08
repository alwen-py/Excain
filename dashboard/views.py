from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import DashBoardLoginForm
from django.contrib import messages

@login_required
def dashboard(request):
    return render(request, 'dashboard/admin/dash/basic.html')


def dashlogin(request):
    return render(request, 'dashboard/admin/login-2.html')


def users(request):
    return render(request, 'dashboard/admin/users.html')


def layouts(request):
    return render(request, 'dashboard/admin/forms/layouts.html')


def login_view(request):
    form = DashBoardLoginForm(request.POST or None)
    msg = None
    if request.method == "POST":
        if form.is_valid():
            msg = "in valid"
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_superuser:
                    login(request, user)
                    messages.success(request, 'Login Successful.')
                    return render(request, "dashboard/admin/dash/basic.html", {"form": form, "msg": msg})
            else:
                messages.error(request, 'Wrong Username or Password ')
                messages.error(request, form.errors)
        else:
            messages.error(request, 'second else')
    return render(request, "dashboard/admin/login-2.html", {"form": form, "msg": msg})

