from django.urls import path
from . import views
urlpatterns = [
    path("", views.forumView, name="forum"),
    path("topic/<int:id>/", views.postForm, name='topic_id'),
    path("new_post", views.topicForm, name="new_post"),
    path("topic/<int:id>/delete", views.topicDelete, name="topic_delete"),
    path("post/<int:post_id>/delete", views.postDelete, name="post_delete")
]
