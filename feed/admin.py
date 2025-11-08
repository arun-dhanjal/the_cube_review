from django.contrib import admin
from .models import Post, Comment

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    Admin configuration for :model:`feed.Post`.

    Displays post metadata and approval status.

    Includes a custom action to bulk-approve selected posts.
    """
    list_display = (
        "__str__",
        "author",
        "created_at",
        "updated_at",
        "is_approved",
    )
    list_filter = ("author", "is_approved",)
    actions = ["approve_posts"]

    def approve_posts(self, request, queryset):
        """Bulk-approve selected posts."""
        queryset.update(is_approved=True)
    approve_posts.short_description = "Approve selected posts"


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Admin configuration for :model:`feed.Comment`.

    Displays comment metadata and approval status.

    Includes a custom action to bulk-approve selected comments.
    """
    list_display = (
        "__str__",
        "author",
        "created_at",
        "updated_at",
        "is_approved",
    )
    list_filter = ("author", "is_approved",)
    actions = ["approve_comments"]
    ordering = ("-created_at",)

    def approve_comments(self, request, queryset):
        """Bulk-approve selected comments."""
        queryset.update(is_approved=True)
    approve_comments.short_description = "Approve selected comments"
