from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    """
    Form for creating or editing a post.

    Includes an optional checkbox to remove the current image.
    """
    remove_image = forms.BooleanField(
        required=False,
        label="Remove current image"
    )

    class Meta:
        model = Post
        fields = ["body", "image"]
        widgets = {
            "image": forms.FileInput(attrs={"class": "form-control"}),
        }


class CommentForm(forms.ModelForm):
    """
    Form for creating or editing a comment on a post.
    """
    class Meta:
        model = Comment
        fields = ["body"]
