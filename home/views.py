from django.shortcuts import render
from dashboard.models import *


def index(request):
    program = Program.objects.all()
    return render(request, 'home/index.html', {"program": program})


def gallery(request):
    return render(request, 'gallery.html')


def contactUs(request):
    message = None
    if request.method =="POST":
      name = request.POST.get('name')
      phone = request.POST.get('phone')
      email = request.POST.get('email')
      subject = request.POST.get('subject')
      message = request.POST.get('message')
      Reachouts.objects.create(name=name,email=email,phone=phone,subject=subject,message=message)
      message = {"context":"your query submitted successfully"}
    return render(request, 'contact-us.html',message)


def courses(request):
  program = Program.objects.all()
  return render(request, 'courses.html', {"program": program,"count":program.count})


def aboutUs(request):
    return render(request, 'about-us.html')


def courseDetail(request, id):
  course = Program.objects.get(pk=id)
  context = {'course': course}
  return render(request, 'single-course.html', context)



