from django.contrib import admin
from .models import Employee,Musician,Album,Student,Projects,Publication,Article,Place,Restaurant

#this is used to work with admin database models
class EmployeeAdmin(admin.ModelAdmin):
    list_display=("empname","contact","joined")
    search_fields=("empname__startswith",)
    
admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Musician)
admin.site.register(Album)
admin.site.register(Student)
admin.site.register(Projects)
admin.site.register(Publication)
admin.site.register(Article)
admin.site.register(Place)
admin.site.register(Restaurant)
# Register your models here.
