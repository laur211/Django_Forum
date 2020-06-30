from django.forms import ModelForm
from .models import ForumModel

class ForumForm(ModelForm):
    class Meta:
        model = ForumModel
        fields = ["title", "content"]