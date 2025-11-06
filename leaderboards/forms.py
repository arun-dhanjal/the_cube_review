from django import forms
from .models import TimeSubmission


class TimeSubmissionForm(forms.ModelForm):
    """
    Form for submitting a :model:`leaderboard.TimeSubmission`.

    Collects puzzle selection and time components (hours, minutes, seconds).

    **Fields**

    ``puzzle``
        The puzzle being solved.
    ``hours``
        Hours component of the time.
    ``minutes``
        Minutes component of the time.
    ``seconds``
        Seconds component of the time.
    """
    class Meta:
        """
        Metadata for :form:`leaderboard.TimeSubmissionForm`.

        Specifies model, fields, and input widgets.
        """
        model = TimeSubmission
        fields = ["puzzle", "hours", "minutes", "seconds"]
        widgets = {
            "hours": forms.NumberInput(attrs={
                "min": 0,
                "max": 24,
                "placeholder": "Hours"
            }),
            "minutes": forms.NumberInput(attrs={
                "min": 0,
                "max": 59,
                "placeholder": "Minutes"
            }),
            "seconds": forms.NumberInput(attrs={
                "min": 0,
                "max": 59,
                "placeholder": "Seconds"
            }),
        }
