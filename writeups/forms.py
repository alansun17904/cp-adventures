from django import forms
from writeups.models import Post
from martor.fields import MartorFormField


class PostForm(forms.ModelForm):
    text = MartorFormField

    class Meta:
        model = Post
        fields = ('title', 'url', 'text', 'tags')


