from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page_feed, name="home_page_feed"),
]