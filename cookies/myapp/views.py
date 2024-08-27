from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(request):
    theme = request.COOKIES.get('theme', 'light')
    return render(request, 'base.html', {'theme': theme})

def set_theme(request, theme):
    if theme in ['light', 'dark']:
        response = redirect('index')
        response.set_cookie('theme', theme, max_age=60*60*24*30)  # Cookie expires in 30 days
        return response
    return redirect('index')
