from django.urls import path
from . import views

urlpatterns = [
    path("", views.PuzzleList.as_view(), name="puzzle_list"),
]
