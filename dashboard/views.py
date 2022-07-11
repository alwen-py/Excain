from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login
from .forms import DashBoardLoginForm
from django.contrib import messages
from django.contrib.auth import *
from django.contrib.auth.forms import *
from django.views.generic import ListView
from django.contrib.auth.models import User

@login_required
def dashboard(request):
    return render(request, 'dashboard/admin/dash/basic.html')


def dashlogin(request):
    return render(request, 'dashboard/admin/login-2.html')


class UserListView(ListView):
    model = User
    template_name = 'dashboard/admin/users.html'


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



def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('/')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'dashboard/admin/change_password.html', {'form': form})
