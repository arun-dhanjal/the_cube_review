from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    remove_image = forms.BooleanField(required=False, label="Remove current image")

    class Meta:
        model = Post
        fields = ["body", "image"]
        widgets = {
            "image": forms.FileInput(attrs={"class": "form-control"}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["body"]