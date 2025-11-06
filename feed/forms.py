from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    """
    Form for creating or editing a :model:`feed.Post`.

    Includes an optional checkbox to remove the current image.

    **Fields**

    ``body``
        The main content of the post.
    ``image``
        An optional image attached to the post.
    ``remove_image``
        A checkbox to remove the current image (not stored in the model).
    """
    remove_image = forms.BooleanField(
        required=False,
        label="Remove current image"
    )

    class Meta:
        """
        Metadata for :form:`feed.PostForm`.

        Specifies model, fields, and widget customization.
        """
        model = Post
        fields = ["body", "image"]
        widgets = {
            "image": forms.FileInput(attrs={"class": "form-control"}),
        }


class CommentForm(forms.ModelForm):
    """
    Form for creating or editing a :model:`feed.Comment`.

    **Fields**

    ``body``
        The content of the comment.
    """
    class Meta:
        """
        Metadata for :form:`feed.CommentForm`.

        Specifies model and fields.
        """
        model = Comment
        fields = ["body"]
