from django import forms
from viewapp.models import User

class UserForm(forms.ModelForm):
   class Meta:
      model = User
      fields = ('name', 'email')