from django.contrib import admin
from .models import Profile,Hobby,Post
# Register your models here.

admin.site.register(Profile)
admin.site.register(Hobby)
admin.site.register(Post)