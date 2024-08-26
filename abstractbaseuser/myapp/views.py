from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserSignupForm
# Create your views here.
def render_page(request):
    return render(request,"index.html",{
        'django':'hello guys my name is sushil lodhi and I am here to support you'
    })

def register(request):
    if request.method=='POST':
        form=UserSignupForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=UserSignupForm()
    
    return render(request,'index.html',{'form':form})
      