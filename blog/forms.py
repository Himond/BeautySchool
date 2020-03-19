from .models import Comment, Postlike
from django import forms
from django.contrib.auth.models import User

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class LikeForm(forms.ModelForm):
    class Meta:
        model = Postlike
        fields = ('post_likes',)