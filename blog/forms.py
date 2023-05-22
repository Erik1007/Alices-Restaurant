from .models import Post
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('body',)