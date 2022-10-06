from django.shortcuts import render
from jobs.models import Job
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    index = Job.objects.all()
    paginator = Paginator(index,6)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)
    context = {'jobs':index,'pag':page_object}
    return render(request,'home/index.html',context)