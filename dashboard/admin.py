from django.contrib import admin

from dashboard.models import *


class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'zone', 'description', 'calling_code')
    search_fields = ['name', 'calling_code']
    ordering = ('name',)
    list_filter = ('name', 'calling_code')


class StateAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'description')
    search_fields = ['name', 'country']
    ordering = ('name',)
    list_filter = ('name', 'country')


class DistrictAdmin(admin.ModelAdmin):
    list_display = ('name', 'state', 'description')
    search_fields = ['name', 'state']
    ordering = ('name',)
    list_filter = ('name', 'state')


class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')
    search_fields = ['name', 'country']
    ordering = ('name',)
    list_filter = ('name', 'country')


class CourseProgramAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at')
    search_fields = ['name', 'created_at']
    ordering = ('-created_at',)
    list_filter = ('name', 'created_at')


class CourseDetailAdmin(admin.ModelAdmin):
    list_display = ('course_program', 'name', 'description', 'created_at')
    search_fields = ['name', 'created_at', 'is_active']
    ordering = ('-created_at',)
    list_filter = ('name', 'created_at')


class LocationAdmin(admin.ModelAdmin):
    list_display = ('street', 'city', 'district', 'state', 'country', 'pincode')
    search_fields = ['city', 'district', 'state', 'country', 'pincode']
    ordering = ('city',)


class ProgramAdmin(admin.ModelAdmin):
    list_display = ('name', 'course_detail', 'description', 'created_at', 'start_date', 'end_date', 'location', 'type')
    search_fields = ['name', 'created_at']
    ordering = ('-created_at',)
    list_filter = ('name', 'created_at')


class ReachoutsAdmin(admin.ModelAdmin):
  list_display = ('name', 'phone', 'email', 'subject')
  search_fields = ['name', 'created_at']
  ordering = ('-created_at',)
  list_filter = ('name', 'created_at')


admin.site.register(Country, CountryAdmin)
admin.site.register(Reachouts,ReachoutsAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(District, DistrictAdmin)
admin.site.register(Currency, CurrencyAdmin)
admin.site.register(CourseProgram, CourseProgramAdmin)
admin.site.register(CourseDetail, CourseDetailAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Program, ProgramAdmin)
