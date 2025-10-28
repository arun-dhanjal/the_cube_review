from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.views import generic
from .models import Post, Comment
from .forms import PostForm, CommentForm

# Create your views here.


class Feed(generic.ListView):
    queryset = Post.objects.filter(is_approved=True)
    template_name = "feed/feed.html"
    context_object_name = "posts"
    paginate_by = 3


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()
    form = CommentForm

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect("post_detail", pk=post.pk)

    return render(request, "feed/post_detail.html", {
        "post": post,
        "comments": comments,
        "form": form,
    })


@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("feed")
    else:
        form = PostForm()
    return render(request, "feed/create_post.html", {"form": form})


@login_required
def edit_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if comment.author != request.user:
        return HttpResponseForbidden("You can't edit this comment.")

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect("post_detail", pk=comment.post.pk)

    else:
        form = CommentForm(instance=comment)

    return render(request, "feed/edit_comment.html", {
        "form": form,
        "comment": comment,
    })
