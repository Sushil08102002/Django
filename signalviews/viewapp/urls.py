# myapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page URL pattern
    path('register/', views.register_user, name='register_user'),
    # other patterns
]
