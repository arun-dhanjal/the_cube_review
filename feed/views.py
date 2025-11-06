from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseForbidden
from django.views import generic
from django.db import models
from .models import Post, Comment
from .forms import PostForm, CommentForm

# Create your views here.


class Feed(generic.ListView):
    """
    Displays a paginated list of :model:`feed.Post` entries.

    Includes unapproved posts authored by the current user.

    **Context**

    ``posts``
        A queryset of :model:`feed.Post` objects.

    **Template**

    :template:`feed/feed.html`
    """
    template_name = "feed/feed.html"
    context_object_name = "posts"
    paginate_by = 5

    def get_queryset(self):
        """
        Conditional queryset to ensure that consistent number of posts
        appear on page regardless of any unapproved posts in feed.
        """
        user = self.request.user
        if user.is_authenticated:
            return (
                Post.objects
                .filter(models.Q(is_approved=True) | models.Q(author=user))
                .order_by("-created_at")
            )
        else:
            return (
                Post.objects
                .filter(is_approved=True)
                .order_by("-created_at")
            )


def post_detail(request, pk):
    """
    Displays an individual :model:`feed.Post` and its comments.

    Handles comment submission for authenticated users.

    **Context**

    ``post``
        An instance of :model:`feed.Post`.
    ``comments``
        A queryset of related :model:`feed.Comment` objects.
    ``form``
        An instance of :form:`feed.CommentForm`.

    **Template**

    :template:`feed/post_detail.html`
    """
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()
    form = CommentForm()

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.success(
                request,
                "Comment added - now pending approval. "
                "Comments will only show to other users once approved."
            )
            return redirect("post_detail", pk=post.pk)

    return render(request, "feed/post_detail.html", {
        "post": post,
        "comments": comments,
        "form": form,
    })


@login_required
def create_post(request):
    """
    Allows authenticated users to create a new :model:`feed.Post`.

    Posts are marked pending approval after submission.

    **Context**

    ``form``
        An instance of :form:`feed.PostForm`.

    **Template**

    :template:`feed/create_post.html`
    """
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(
                request,
                "New post added - now pending approval. "
                "Posts will only show on the public feed once approved."
            )
            return redirect("feed")
    else:
        form = PostForm()
    return render(request, "feed/create_post.html", {"form": form})


@login_required
def edit_post(request, pk):
    """
    Allows post authors to edit their :model:`feed.Post`.

    Resets approval status and optionally removes the image.

    **Context**

    ``form``
        An instance of :form:`feed.PostForm`.
    ``post``
        The :model:`feed.Post` being edited.

    **Template**

    :template:`feed/edit_post.html`
    """
    post = get_object_or_404(Post, pk=pk)
    if post.author != request.user:
        return HttpResponseForbidden("You can't edit this post.")

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            if form.cleaned_data.get("remove_image"):
                post.image = None
            post.is_approved = False
            post.save()
            messages.success(
                request,
                "Post edited successfully - status "
                "changed to 'Pending approval'."
            )
            return redirect("post_detail", pk=post.pk)
    else:
        form = PostForm(instance=post)

    return render(request, "feed/edit_post.html", {
        "form": form,
        "post": post,
    })


@login_required
def delete_post(request, pk):
    """
    Allows post authors to delete their :model:`feed.Post`.

    Redirects to the feed after deletion.
    """
    post = get_object_or_404(Post, pk=pk)
    if post.author != request.user:
        return HttpResponseForbidden("You can't delete this post.")

    post.delete()
    messages.success(request, "Post deleted successfully.")
    return redirect("feed")


@login_required
def edit_comment(request, pk):
    """
    Allows comment authors to edit their :model:`feed.Comment`.

    Resets approval status after editing.

    **Context**

    ``form``
        An instance of :form:`feed.CommentForm`.
    ``comment``
        The :model:`feed.Comment` being edited.

    **Template**

    :template:`feed/edit_comment.html`
    """
    comment = get_object_or_404(Comment, pk=pk)
    if comment.author != request.user:
        return HttpResponseForbidden("You can't edit this comment.")

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.is_approved = False
            comment.save()
            messages.success(
                request,
                "Comment edited successfully - status changed "
                "to 'Pending approval'."
            )
            return redirect("post_detail", pk=comment.post.pk)

    else:
        form = CommentForm(instance=comment)

    return render(request, "feed/edit_comment.html", {
        "form": form,
        "comment": comment,
    })


@login_required
def delete_comment(request, pk):
    """
    Allows comment authors to delete their :model:`feed.Comment`.

    Redirects to the related post after deletion.
    """
    comment = get_object_or_404(Comment, pk=pk)
    if comment.author != request.user:
        return HttpResponseForbidden("You can't delete this comment.")

    post_pk = comment.post.pk
    comment.delete()
    messages.success(request, "Comment deleted successfully.")
    return redirect("post_detail", pk=post_pk)
