from django.db import models

# Create your models here.
class Profile(models.Model):
    display_name = models.CharField(max_length=30)
    mobile = models.IntegerField()
    address = models.TextField()
    email = models.EmailField()
    dob = models.DateField()
    photo=models.FileField(upload_to='profile/',null=True,blank=True)
    status = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Hobby(models.Model):   
    user=models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='user_hobby',null=True,blank=True)
    name = models.CharField(max_length=30)
    description = models.TextField()
    status = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class Books(models.Model):
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=20)
    genere=models.CharField(max_length=30)
    
    def __str__(self):
        return self.title