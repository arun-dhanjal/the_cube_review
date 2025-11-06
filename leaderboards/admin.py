from django.contrib import admin
from .models import TimeSubmission

# Register your models here.


@admin.register(TimeSubmission)
class TimeSubmissionAdmin(admin.ModelAdmin):
    """
    Admin configuration for :model:`leaderboard.TimeSubmission`.

    Displays submission string, puzzle, and user.
    """
    list_display = ("__str__", "puzzle", "user")
    list_filter = ("puzzle", "user")
