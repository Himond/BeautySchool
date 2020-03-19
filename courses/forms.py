from django.contrib.auth.models import User
from django import forms
from .models import CourseEntry

class EntryForm(forms.ModelForm):
    class Meta:
        model = CourseEntry
        fields = ('first_name', 'last_name', 'email', 'phone',  'comments')
