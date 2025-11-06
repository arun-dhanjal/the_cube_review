from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    """
    Form for creating or editing a :model:`reviews.Review`.

    **Fields**

    ``rating``
        The numerical rating given to the puzzle.
    ``body``
        The written content of the review.
    """
    class Meta:
        """
        Metadata for :form:`reviews.ReviewForm`.

        Specifies model and fields.
        """
        model = Review
        fields = ["rating", "body"]
