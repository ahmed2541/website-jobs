from distutils.command.upload import upload
from email.mime import image
from django.db import models

# Create your models here.
class AboutAdmin(models.Model):
    image = models.ImageField(upload_to='admin_photos/%y/%m/%d',default='admin_photos/22/10/05/IMG_20220227_200036_660.jpg')
    def __str__(self):
        return str(self.image)