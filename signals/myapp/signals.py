from django.db.models.signals import post_save
from django.dispatch import receiver  
from myapp.models import User
# from django.core.mail import send_mail 


@receiver(post_save,sender=User)
def user_created(sender,instance,created,**kwargs):
    if created:
        print('A new user was created: ',instance.name, instance.email)
        