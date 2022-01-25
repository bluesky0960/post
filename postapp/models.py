from django.db import models
from ckeditor.fields import RichTextField

class Post(models.Model):
    subject = models.CharField(max_length=200)
    content = RichTextField()
    register_date = models.DateTimeField()

    def __str__(self):
        return self.subject

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = RichTextField()
    register_date = models.DateTimeField()