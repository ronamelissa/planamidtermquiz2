from django.forms import ModelForm
from .models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        exclude = ['id']
        ordering=['date_updated']
