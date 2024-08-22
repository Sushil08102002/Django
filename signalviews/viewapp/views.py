# myapp/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login



def home(request):
    return render(request,'home.html')
def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Send welcome email directly in the view
            print('A new user is created')
            login(request, user)  # Optional: Log the user in after registration
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'base.html', {'form': form})
