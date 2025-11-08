from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.


class Post(models.Model):
    """
    Represents a user-created :model:`feed.Post` with optional image.

    Includes approval status and timestamps for moderation and display
    ordering.

    Related to :model:`auth.User` via the ``author`` field.

    **Fields**

    ``body``
        The main content of the post.
    ``image``
        An optional image uploaded via Cloudinary.
    ``author``
        The user who created the post.
    ``created_at``
        Timestamp of post creation.
    ``updated_at``
        Timestamp of last update.
    ``is_approved``
        Whether the post is approved for public display.

    **Meta**

    ``ordering``
        Posts are ordered by creation time (newest first).
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
        """
        Returns a readable string representation of the post.
        """
        return (
            f"Post by {self.author.username} on "
            f"{self.created_at.strftime('%Y-%m-%d %H:%M')}"
        )


class Comment(models.Model):
    """
    Represents a :model:`feed.Comment` made by a user on a specific post.

    Includes approval status and timestamps for moderation and display
    ordering.

    Related to :model:`auth.User` via the ``author`` field,
    and to :model:`feed.Post` via the ``post`` field.

    **Fields**

    ``body``
        The content of the comment.
    ``author``
        The user who wrote the comment.
    ``post``
        The post being commented on.
    ``created_at``
        Timestamp of comment creation.
    ``updated_at``
        Timestamp of last update.
    ``is_approved``
        Whether the comment is approved for public display.

    **Meta**

    ``ordering``
        Comments are ordered by creation time (oldest first).
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
        """
        Returns a readable string representation of the comment.
        """
        return (
            f"Comment by {self.author.username} on "
            f"{self.created_at.strftime('%Y-%m-%d %H:%M')}"
        )
