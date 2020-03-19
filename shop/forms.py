from django.contrib.auth.models import User
from django import forms
from .models import ReviewStudio


class ReviewStudioForm(forms.ModelForm):
    class Meta:
        model = ReviewStudio
        fields = ('studio_review',)