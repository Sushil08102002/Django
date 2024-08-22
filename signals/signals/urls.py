from django.contrib import admin
from django.urls import path, include

urlpatterns = [
   path('admin/', admin.site.urls),
   # here, firstApp is a app name
   path('', include("myapp.urls")),
]