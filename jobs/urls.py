from django.urls import path
from . import views

####################
app_name = 'jobs'

urlpatterns = [
    path('',views.job_list,name='job_list'),

    path('<str:slug>/',views.job_detail,name='job_detail'),
    path('apply_job/<str:slug>/',views.apply_job,name='apply_job'),
]