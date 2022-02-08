from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import DashBoardLoginForm


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
                    msg = 'Login successful'
                    return render(request, "dashboard/admin/dash/basic.html", {"form": form, "msg": msg})
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'
    return render(request, "dashboard/admin/login-2.html", {"form": form, "msg": msg})

