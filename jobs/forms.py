from dataclasses import fields

from django import forms
from .models import Apply


class ApplyForm(forms.ModelForm):
    class Meta:
        model = Apply
        fields = '__all__'
        exclude = ('user','date_and_time')

