from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required

# Create your views here.


class Feed(generic.ListView):
    queryset = Post.objects.filter(is_approved=True)
    template_name = "feed/feed.html"
    context_object_name = "posts"
    paginate_by = 3


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.filter(is_approved=True)
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
