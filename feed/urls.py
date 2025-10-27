from django.urls import path
from . import views

urlpatterns = [
    path("", views.Feed.as_view(), name="feed"),
    path("create/", views.create_post, name="create_post"),
    path("post/<int:pk>/", views.post_detail, name="post_detail"),
]
