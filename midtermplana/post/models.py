from django.db import models
from datetime import datetime
from django.utils.timezone import now
# Create your models here.
class Post(models.Model):
    title_text = models.CharField(max_length=100)
    date_created = models.DateTimeField(default=now)
    date_updated = models.DateTimeField(default=now)
    content_text = models.TextField(max_length=300)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title_text


class Comment(models.Model):
    date_created_comment = models.DateTimeField('date created')
    content_text_comment = models.TextField(max_length=300)
    post_text = models.ForeignKey('post.Post', on_delete=models.CASCADE, related_name='comments')
