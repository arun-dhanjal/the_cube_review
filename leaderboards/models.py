from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from reviews.models import Puzzle

# Create your models here.


class TimeSubmission(models.Model):
    puzzle = models.ForeignKey(Puzzle, related_name="times", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    hours = models.PositiveIntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(24)]
    )
    minutes = models.PositiveIntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(59)]
    )
    seconds = models.PositiveIntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(59)]
    )

    total_seconds = models.PositiveIntegerField(editable=False)

    submitted_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["total_seconds"]
        unique_together = ("user", "puzzle")  # Ensures only one user submission per puzzle

    # Ensures zero times can't be submitted
    def clean(self):
        if self.hours == 0 and self.minutes == 0 and self.seconds == 0:
            raise ValidationError("Time must be greater than zero.")

    # Saves total_seconds as its own field based on inputs of hours, minutes, and seconds
    def save(self, *args, **kwargs):
        self.total_seconds = self.hours * 3600 + self.minutes * 60 + self.seconds
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user} | {self.puzzle} | {self.hours}h {self.minutes}m {self.seconds}s"
