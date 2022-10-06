from datetime import datetime
from distutils.command.upload import upload
from email.policy import default
from random import choices
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.




class Job(models.Model):
    title = models.CharField(max_length=150,default='')
    salary = models.IntegerField(default=500)
    location = models.CharField(default='',max_length=150)
    image = models.ImageField(upload_to='photos/%y/%m/%d')
    created_at = models.DateTimeField(default=datetime.now)
    description = models.TextField(default='')
    content = models.CharField(max_length=75,null=True,blank=True) 
    slug = models.CharField(max_length=750,null=True,blank=True) 

    def save(self,*args,**kwargs):
        self.slug =slugify(self.title) 
        self.content = self.description
        super(Job,self).save(*args,**kwargs)



    def __str__(self):
        return self.title


Gender =[ 
    ('male','male'),
    ('female','female')
    ]

class Apply(models.Model):
    user =models.ForeignKey(User,related_name='job_apply',on_delete=models.CASCADE)
    job = models.ForeignKey('Job', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50, choices=Gender)
    country = models.CharField(max_length=100)
    email = models.EmailField(max_length=250)
    cv = models.FileField(upload_to='cv/%y/%m/%d')
    your_skills = models.TextField(default='')
    date_and_time = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name


