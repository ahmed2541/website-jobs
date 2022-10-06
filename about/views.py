
from django.shortcuts import render
from .models import AboutAdmin
# Create your views here.
def about(request):
    image = AboutAdmin.objects.all()
    return render(request,'about/about.html',{'image':image} )