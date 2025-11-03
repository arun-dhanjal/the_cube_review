from django.urls import path
from . import views

urlpatterns = [
    path("", views.PuzzleList.as_view(), name="puzzle_list"),
    path("<int:pk>/", views.puzzle_detail, name="puzzle_detail"),
    path("review/<int:pk>/edit/", views.edit_review, name="edit_review"),
    path("review/<int:pk>/delete/", views.delete_review, name="delete_review"),
]
