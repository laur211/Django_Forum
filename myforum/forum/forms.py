from django.forms import ModelForm
from .models import TopicModel

class ForumForm(ModelForm):
    class Meta:
        model = TopicModel
        fields = ["title", "content"]