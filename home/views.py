from django.shortcuts import render

from dashboard.models import Program


def index(request):
    program = Program.objects.all()
    return render(request, 'home/index.html', {"program": program})


def gallery(request):

    return render(request, 'gallery.html')


def contactus(request):

    return render(request, 'contact-us.html')


def aboutus(request):

    return render(request, 'about-us.html')

