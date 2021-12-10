from django import forms
from writeups.models import Post


class PostFrom(forms.ModelForm):

    class Meta:
        model = Post
