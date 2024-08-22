from django.shortcuts import render
from myapp.forms import UserForm
# Create your views here.
def create_user(request):
   # If the form is submitted, save the user. Otherwise, just create an empty form.
   if request.method == 'POST':
      form = UserForm(request.POST)
      if form.is_valid():
         form.save()
   else:
      form = UserForm()
      # send the base.html file on the response.
   return render(request, 'base.html', {'form': form})