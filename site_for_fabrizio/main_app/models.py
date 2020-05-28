from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='images')
    created_date = models.DateTimeField(default=timezone.now)
# Create your models here.
