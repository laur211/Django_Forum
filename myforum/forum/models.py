from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class ForumModel(models.Model):
    title = models.CharField (max_length=100)
    posted = models.DateTimeField(auto_now=True)
    content = models.CharField(max_length=255, blank=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)