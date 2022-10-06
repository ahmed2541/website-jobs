
from contextlib import redirect_stderr
from django.shortcuts import render
from .models import Job
from .filters import JobFilter
from django.core.paginator import Paginator
from .forms import ApplyForm
from contact.models import Info

# Create your views here.

#for all jobs
def job_list(request):
    job_list = Job.objects.all()

    #filter 
    myfilter = JobFilter(request.GET , queryset=job_list)
    job_list = myfilter.qs

    #paginator
    paginator = Paginator(job_list,4)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)

    context = {'jobs':page_object,'myfilter':myfilter} 
    return render(request,'job/job_list.html',context)    




#for one job or detail
def job_detail(request,slug):
    job_detail = Job.objects.get(slug=slug)

#contact detail
    info = Info.objects.all()    

    context = {'job':job_detail,'info':info}
    return render(request,'job/job_detail.html',context)

def apply_job(request,slug):
    job_detail = Job.objects.get(slug=slug)

    #apply for a job

    if request.method=='POST':
        form = ApplyForm(request.POST,request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.user = request.user
            myform.job = job_detail
            myform.save()
            print('doo00ne')      

    else :
        form = ApplyForm()

    context = {'form1':form}
    return render(request,'job/apply_job.html',context)    

def index(request):
    return render(request,'home/index.html')