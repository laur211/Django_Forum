from django.shortcuts import render, redirect
from .models import TopicModel, PostModel
from .forms import ForumForm
# Create your views here.


def forumView(request):
    topics = TopicModel.objects.all()
    return render (request, "forum/index.html", {"topics": topics})


def topicForm(request):
    if request.method == "POST":
        form = ForumForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get("title")
            TopicModel.objects.create (title=title, autor=request.user)
            return redirect ("forum")
    else:
        form = ForumForm()
    return render(request, "forum/postsform.html", {"form": form})


def postForm(request, id):
    if request.method == "POST":
        form = ForumForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get("title")
            PostModel.objects.create (title=title, autor=request.user, topic=TopicModel.objects.get(id=id))
    else:
        form = ForumForm()
    topics = TopicModel.objects.filter(id=id).values()
    posts = PostModel.objects.filter(topic=TopicModel.objects.get(id=id))
    return render(request, "forum/postsform.html", {"form": form, "topics": topics, "posts": posts})


def topicDelete(request, id):
    topic = TopicModel.objects.get(id=id)
    topic.delete()
    return redirect("forum")


def postDelete(request, post_id):
    post = PostModel.objects.get(id=post_id)
    post.delete()
    return redirect("forum")
