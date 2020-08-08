from django.contrib import admin
from .models import TopicModel, PostModel
# Register your models here.
admin.site.register(TopicModel)
admin.site.register(PostModel)