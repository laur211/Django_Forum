from django.shortcuts import render
from .models import ForumModel
# Create your views here.


def forumView(request):
    posts = ForumModel.objects.all()
    return render (request, "forum/index.html", {"posts": posts})