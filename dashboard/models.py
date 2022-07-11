from django.db import models
from djrichtextfield.models import RichTextField
# Create your models here.
from django.utils.timezone import now


class Country(models.Model):
    name = models.CharField(max_length=40, null=True, blank=True)
    zone = models.CharField(max_length=40, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    calling_code = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


class State(models.Model):
    name = models.CharField(max_length=40, null=True, blank=True)
    country = models.ForeignKey(Country, null=False, blank=False, on_delete=models.CASCADE)
    description = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField(max_length=40, null=True, blank=True)
    state = models.ForeignKey(State, null=False, blank=False, on_delete=models.CASCADE)
    description = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name


class Currency(models.Model):
    name = models.CharField(max_length=40, null=True, blank=True)
    country = models.ForeignKey(Country, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class CourseProgram(models.Model):
    name = models.CharField(max_length=40, null=True, blank=True)
    description = RichTextField()
    created_at = models.DateTimeField(default=now, null=False, blank=False)

    def __str__(self):
        return self.name


class CourseDetail(models.Model):
    course_program = models.ForeignKey(CourseProgram, null=False, blank=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True, blank=True)
    description = RichTextField()
    created_at = models.DateTimeField(default=now, null=False, blank=False)

    def __str__(self):
        return self.name


class Location(models.Model):
    street = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    district = models.ForeignKey(District, null=False, blank=False, on_delete=models.CASCADE)
    state = models.ForeignKey(State, null=False, blank=False, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, null=False, blank=False, on_delete=models.CASCADE)
    pincode = models.IntegerField(null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.city


class Program(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    course_detail = models.ForeignKey(CourseDetail, null=False, blank=False, on_delete=models.CASCADE)
    description = RichTextField()
    image = models.ImageField(blank=True, upload_to='program')
    created_at = models.DateTimeField(default=now, null=False, blank=False)
    start_date = models.DateTimeField(null=False, blank=False)
    end_date = models.DateTimeField(null=False, blank=False)
    location = models.ForeignKey(Location, null=False, blank=False, on_delete=models.CASCADE)
    type = models.CharField(max_length=255, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    gst = models.IntegerField(null=True, blank=True)
    duration = models.IntegerField(null=True, blank=True)
    certificate_available = models.BooleanField(default=True, null=False, blank=False)
    is_active = models.BooleanField(default=True, null=False, blank=False)

    def __str__(self):
        return self.name


class Reachouts(models.Model):
  name = models.CharField(max_length=255, null=True, blank=True)
  email = models.CharField(max_length=255, null=True, blank=True)
  phone = models.CharField(max_length=255, null=True, blank=True)
  subject = models.CharField(max_length=255, null=True, blank=True)
  message = models.CharField(max_length=255, null=True, blank=True)
  created_at = models.DateTimeField(default=now, null=False, blank=False)

  def __str__(self):
    return self.name
