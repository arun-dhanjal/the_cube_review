from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.


class Puzzle(models.Model):
    CATEGORY_CHOICES = [
        ('Cube', 'Standard Cube'),
        ('Docecahedron', '12-Sided Puzzle'),
        ('Special', 'Specialty Shape'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    image = CloudinaryField("image")
    description = models.TextField()

    def __str__(self):
        return self.name

    def average_rating(self):
        reviews = self.reviews.filter(is_approved=True)
        total = sum([review.rating for review in reviews])
        count = reviews.count()
        if count > 0:
            return total / count
        return None

    def review_count(self):
        return self.reviews.filter(is_approved=True).count()


class Review(models.Model):
    puzzle = models.ForeignKey(Puzzle, on_delete=models.CASCADE, related_name="reviews")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(choices=[(i, f"{i} stars") for i in range(1, 6)])
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.puzzle.name} review by {self.author.username}"
