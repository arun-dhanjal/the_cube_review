from django.contrib import admin
from .models import Puzzle, Review

# Register your models here.


@admin.register(Puzzle)
class PostAdmin(admin.ModelAdmin):
    list_display = ("__str__",)


@admin.register(Review)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("__str__", "author", "created_at", "is_approved")
    list_filter = ("is_approved",)
    actions = ["approve_reviews"]

    def approve_reviews(self, request, queryset):
        queryset.update(is_approved=True)
    approve_reviews.short_description = "Approved selected reviews"
