from django.contrib import admin
from .models import Post, Comment

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("__str__", "author", "created_at", "is_approved")
    list_filter = ("author", "is_approved",)
    actions = ["approve_posts"]

    def approve_posts(self, request, queryset):
        queryset.update(is_approved=True)
    approve_posts.short_description = "Approve selected posts"


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("__str__", "author", "created_at", "is_approved")
    list_filter = ("author", "is_approved",)
    actions = ["approve_comments"]

    def approve_comments(self, request, queryset):
        queryset.update(is_approved=True)
    approve_comments.short_description = "Approved selected comments"
