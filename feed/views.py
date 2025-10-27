from django.shortcuts import render, redirect
from django.views import generic
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required

# Create your views here.


class Feed(generic.ListView):
    queryset = Post.objects.filter(is_approved=True)
    template_name = "feed/feed.html"
    context_object_name = "posts"
    paginate_by = 3


@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect(feed)
    else:
        form = PostForm()
    return render(request, "feed/create_post.html", {"form": form})
