from django.urls import path
from . import views
urlpatterns = [
    path("", views.forumView, name="forum"),
    path("new_post", views.topicForm, name="new_post"),
    path("post", views.postForm, name="topic_post")
]
