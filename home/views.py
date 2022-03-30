from django.shortcuts import render
from dashboard.models import *
from dashboard.models import Program

from django.views.generic import DetailView


def index(request):
    program = Program.objects.all()
    return render(request, 'home/index.html', {"program": program})


def gallery(request):

    return render(request, 'gallery.html')


def contactus(request):

    return render(request, 'contact-us.html')


def aboutus(request):

    return render(request, 'about-us.html')


def courses(request):

    return render(request, 'courses.html')

def singlecourse(request):

    return render(request, 'single-course.html')



def coursedetail(request,id):
    print(request.GET.get('id'))
    id=id
    
    # course_id=CourseDetail.objects.get(id=c_id)
    # program = {'program': Program.description()}
    
    return render(request, 'single-course.html')

