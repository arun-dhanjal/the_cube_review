from django.contrib import admin
from .models import TimeSubmission

# Register your models here.


@admin.register(TimeSubmission)
class TimeSubmission(admin.ModelAdmin):
    list_display = ("__str__",)