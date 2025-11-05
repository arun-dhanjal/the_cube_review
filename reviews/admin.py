from django.contrib import admin
from .models import Puzzle, Review

# Register your models here.


@admin.register(Puzzle)
class PuzzleAdmin(admin.ModelAdmin):
    list_display = ("name", "category")
    list_filter = ("category",)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("__str__", "puzzle", "author", "created_at", "is_approved")
    list_filter = ("puzzle", "author", "is_approved",)
    actions = ["approve_reviews"]

    def approve_reviews(self, request, queryset):
        queryset.update(is_approved=True)
    approve_reviews.short_description = "Approved selected reviews"
