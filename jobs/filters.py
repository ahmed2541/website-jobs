
from dataclasses import fields
from pyexpat import model
from .models import Job
import django_filters

class JobFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='iconatains')
    description = django_filters.CharFilter(lookup_expr='iconatains')

    class Meta :
        model = Job
        fields = ['title','salary','description']