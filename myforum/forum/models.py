from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.


class TopicModel(models.Model):
    title = models.CharField (max_length=100)
    posted = models.DateTimeField(auto_now=True)
    content = models.CharField(max_length=255, blank=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.id


class PostModel(models.Model):
    title = models.CharField(max_length=100)
    posted = models.DateTimeField(auto_now=True)
    content = models.CharField(max_length=255, blank=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.ForeignKey(TopicModel, on_delete=models.CASCADE)