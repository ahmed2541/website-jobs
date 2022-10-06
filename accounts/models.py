from distutils.command.upload import upload
from email.policy import default
import imp
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,related_name ='signup',on_delete=models.CASCADE)
    location = models.CharField(max_length=100,default='')
    phone_number = models.CharField(max_length=15)
    image = models.ImageField(upload_to='profile_photos/%y/%m/%d',default='/photos/22/10/03/images.jpg')

    def __str__(self) :
        return str(self.user)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
