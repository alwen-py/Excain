from django.shortcuts import render

# Create your views here.

def dash(request):
    return render(request,'dashboard/admin/dash/basic.html')


def dashlogin(request):
    return render(request,'dashboard/admin/login-2.html')
