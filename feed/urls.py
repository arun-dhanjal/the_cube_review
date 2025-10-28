from django.urls import path
from . import views

urlpatterns = [
    path("", views.Feed.as_view(), name="feed"),
    path("create/", views.create_post, name="create_post"),
    path("post/<int:pk>/", views.post_detail, name="post_detail"),
    path("post/<int:pk>/edit", views.edit_post, name="edit_post"),
    path("post/<int:pk>/delete/", views.delete_post, name="delete_post"),
    path("comment/<int:pk>/edit/", views.edit_comment, name="edit_comment"),
    path("comment/<int:pk>/delete/", views.delete_comment, name="delete_comment"),
]
