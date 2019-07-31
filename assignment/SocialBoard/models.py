from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length = 120)
    publish_date = models.DateTimeField()
    content = models.CharField(max_length = 500)
    author = models.CharField(max_length = 24)

