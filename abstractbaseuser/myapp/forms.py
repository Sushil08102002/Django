from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm
    
class UserSignupForm(UserCreationForm):
    email=forms.EmailField()
    first_name=forms.CharField(max_length=100, required=True)
    last_name=forms.CharField(max_length=100)
    is_active=forms.CheckboxInput(check_test="is_active")
    is_admin=forms.CheckboxInput(check_test="is_admin")
    phone=forms.CharField(max_length=20)
    
    class Meta:
        model=CustomUser
        fields=['first_name','last_name','email','phone','password1','password2']
        
    