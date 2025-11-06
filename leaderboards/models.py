from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from reviews.models import Puzzle

# Create your models here.


class TimeSubmission(models.Model):
    """
    Represents a time-based submission for a :model:`reviews.Puzzle`.

    Stores hours, minutes, and seconds, and calculates total time in seconds.

    **Fields**

    ``puzzle``
        The puzzle being solved.
    ``user``
        The user who submitted the time.
    ``hours``, ``minutes``, ``seconds``
        Time components with validation.
    ``total_seconds``
        Computed total time in seconds (non-editable).
    ``submitted_at``
        Timestamp of submission.

    **Meta**

    ``ordering``
        Submissions are ordered by total time.
    ``unique_together``
        Each user can submit only one time per puzzle.
    """
    puzzle = models.ForeignKey(
        Puzzle,
        related_name="times",
        on_delete=models.CASCADE
        )
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

    class Meta:
        ordering = ["total_seconds"]
        unique_together = ("user", "puzzle")

    def clean(self):
        """
        Validates that the submitted time is greater than zero.
        """
        if self.hours == 0 and self.minutes == 0 and self.seconds == 0:
            raise ValidationError("Time must be greater than zero.")

    def save(self, *args, **kwargs):
        """
        Calculates and stores total time in seconds before saving.
        """
        self.total_seconds = (
            self.hours * 3600 + self.minutes * 60 + self.seconds
        )
        super().save(*args, **kwargs)

    def __str__(self):
        """
        Returns a readable string representation of the submission.
        """
        return (
            f"{self.user} | {self.puzzle} | "
            f"{self.hours}h {self.minutes}m {self.seconds}s"
        )
