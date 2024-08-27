from django.shortcuts import render, redirect

def index(request):
    # Retrieve theme from cookies 
    theme = request.COOKIES.get('theme', 'light')
    return render(request, 'base.html', {'theme': theme})

def set_theme(request, theme):
    response = redirect('index')  # Redirect to the main page
    if theme in ['light', 'dark']:
        response.set_cookie('theme', theme, max_age=60*60*24*30)  # Cookie expires in 30 days
    return response
