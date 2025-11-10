from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.


class Puzzle(models.Model):
    """
    Represents a puzzle that users can review.

    Includes category, image, and description.

    **Fields**

    ``name``
        The puzzle's name.
    ``category``
        The puzzle's category (Cube, Dodecahedron, Special).
    ``image``
        An image of the puzzle, stored via Cloudinary.
    ``description``
        A textual description of the puzzle.
    """
    CATEGORY_CHOICES = [
        ('Cube', 'Cube'),
        ('Dodecahedron', 'Dodecahedron'),
        ('Special', 'Special'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    image = CloudinaryField("image")
    description = models.TextField()

    def __str__(self):
        """
        Returns the puzzle's name.
        """
        return self.name

    def average_rating(self):
        """
        Calculates the average rating from approved reviews.

        Returns ``None`` if there are no approved reviews.
        """
        reviews = self.reviews.filter(is_approved=True)
        total = sum([review.rating for review in reviews])
        count = reviews.count()
        if count > 0:
            return total / count
        return None

    def review_count(self):
        """
        Returns the number of approved reviews for the puzzle.
        """
        return self.reviews.filter(is_approved=True).count()


class Review(models.Model):
    """
    Represents a user-submitted review for a :model:`reviews.Puzzle`.

    Includes rating, body, timestamps, and approval status.

    **Fields**

    ``puzzle``
        The puzzle being reviewed.
    ``author``
        The user who wrote the review.
    ``rating``
        A score from 1 to 5 stars.
    ``body``
        The written content of the review.
    ``created_at``
        Timestamp of review creation.
    ``updated_at``
        Timestamp of last update.
    ``is_approved``
        Whether the review is approved for public display.
    """
    puzzle = models.ForeignKey(
        Puzzle,
        on_delete=models.CASCADE,
        related_name="reviews"
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(
        choices=[(i, f"{i} stars") for i in range(1, 6)]
    )
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        """
        Returns a readable string representation of the review.
        """
        return f"{self.puzzle.name} review by {self.author.username}"
