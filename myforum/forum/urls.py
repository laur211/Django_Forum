from django.urls import path
from . import views
urlpatterns = [
    path("", views.forumView, name="forum"),
    path("new_post", views.postsForm, name="posts")
]
