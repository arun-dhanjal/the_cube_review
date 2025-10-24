from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def feed(request):
    posts = Post.objects.filter(is_approved=True)
    return render(request, "feed/feed.html", {"posts": posts})


@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect(home_page_feed)
    else:
        form = PostForm()
    return render(request, "feed/create_post.html", {"form": form})
