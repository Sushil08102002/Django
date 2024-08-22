from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from  newapp.models import Employee,Student


def hello(request):
    language=datetime.now().date()
    return render(request, "index.html",{"today":language})


def credops(request):
    #create an entry
    employee=Employee(
        empno="12",
        empname="Abhinav",
        contact="9977605565",
        salary=4000,
        joined=12-12-25
)
    employee.save()
    return HttpResponse(request)
    
# Create your views here.
