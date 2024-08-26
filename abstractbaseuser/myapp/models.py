from django.contrib.auth.models import UserManager
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
    
class CustomUser(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField(verbose_name='email_address',max_length=255,unique=True)
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    is_active=models.BooleanField(default=True)
    is_admin=models.BooleanField(default=False)
    # password=models.CharField(max_length=16)
    phone=models.CharField(max_length=15,null=True,blank=True)
    
    
    
    objects=UserManager()
    
    USERNAME_FIELD='email'
    REQUIRED_FIELDS =[]

    def __str__(self):
        return self.email
    
    def has_perm(self,perm,obj=None): #this code is used to check which permissions a user have
        return True   
    
    def has_module_perms(self,app_label): #this code checks permission associated with a particular app
        return True
    
    @property
    def is_staff(self):   #check which type of user have access to admin interface
        return self.is_admin
    
