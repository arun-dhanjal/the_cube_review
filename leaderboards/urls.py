from django.urls import path
from . import views

urlpatterns = [
    path("", views.Leaderboards.as_view(), name="leaderboards"),
    path("submit-time/", views.submit_time, name="submit_time"),
    path("update-time/", views.update_time, name="update_time"),
    path("delete-time/", views.delete_time, name="delete_time"),
]