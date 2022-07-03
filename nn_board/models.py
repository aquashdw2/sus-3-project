from django.db import models


class BoardPost(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
