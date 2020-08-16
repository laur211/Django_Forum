from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class TopicModel(models.Model):
    title = models.CharField (max_length=100)
    posted = models.DateTimeField(auto_now=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.id


class PostModel(models.Model):
    title = models.CharField(max_length=100)
    posted = models.DateTimeField(auto_now=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.ForeignKey(TopicModel, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

    def __unicode__(self):
        return self.id

    def get_url(self):
        return reverse("topic_id", kwargs={"id": self.id})