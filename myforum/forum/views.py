from django.shortcuts import render, redirect
from .models import ForumModel
from .forms import ForumForm
# Create your views here.


def forumView(request):
    posts = ForumModel.objects.all()
    print(request.user.id)
    print(request.user.username)
    return render (request, "forum/index.html", {"posts": posts})


def postsForm(request):
    if request.method == "POST":
        form = ForumForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get("title")
            content = form.cleaned_data.get("content")
            ForumModel.objects.create (title=title, content=content, autor=request.user)
            return redirect ("forum")
    else:
        form = ForumForm()
    return render(request, "forum/postsform.html", {"form": form})


