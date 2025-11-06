from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.


class Post(models.Model):
    """
    Represents a user-created post with optional image.
    Includes approval status and timestamps for moderation
    and display ordering.

    Related to :model:`auth.User` via the `author` field.
    """
    body = models.TextField()
    image = CloudinaryField("image", blank=True, null=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="posts"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"Post by {self.author.username} on {self.created_at.strftime('%Y-%m-%d %H:%M')}"


class Comment(models.Model):
    """
    Represents a comment made by a user on a specific post.
    Includes approval status and timestamps for moderation
    and display ordering.

    Related to :model:`auth.User` via the `author` field,
    and to :model:`Post` via the `post` field.
    """
    body = models.TextField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="commenter"
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return (
            f"Comment by {self.author.username} on "
            f"{self.created_at.strftime('%Y-%m-%d %H:%M')}"
        )
