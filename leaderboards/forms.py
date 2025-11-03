from django import forms
from .models import TimeSubmission


class TimeSubmissionForm(forms.ModelForm):
    class Meta:
        model = TimeSubmission
        fields = ["puzzle", "hours", "minutes", "seconds"]
        widgets = {
            "hours": forms.NumberInput(attrs={"min": 0, "max": 24, "placeholder": "Hours"}),
            "minutes": forms.NumberInput(attrs={"min": 0, "max": 59, "placeholder": "Minutes"}),
            "seconds": forms.NumberInput(attrs={"min": 0, "max": 59, "placeholder": "Seconds"}),
        }