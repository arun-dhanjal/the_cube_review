from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseForbidden
from django.views import generic
from .models import Puzzle, Review
from .forms import ReviewForm

# Create your views here.


class PuzzleList(generic.ListView):
    model = Puzzle
    template_name = "reviews/puzzle_list.html"
    context_object_name = "puzzles"
    paginate_by = 3


def puzzle_detail(request, pk):
    puzzle = get_object_or_404(Puzzle, pk=pk)
    reviews = puzzle.reviews.all()
    form = ReviewForm

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.puzzle = puzzle
            review.save()
            messages.success(request, "Review added - now pending approval. Reviews will only show to other users once approved.")
            return redirect("puzzle_detail", pk=puzzle.pk)

    return render(request, "reviews/puzzle_detail.html", {
        "puzzle": puzzle,
        "reviews": reviews,
        "form": form,
    })


@login_required
def edit_review(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if review.author != request.user:
        return HttpResponseForbidden("You can't edit this review.")

    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            review = form.save(commit=False)
            review.is_approved = False
            review.save()
            messages.success(request, "Review edited successfully - status changed to 'Pending approval'.")
            return redirect("puzzle_detail", pk=review.puzzle.pk)

    else:
        form = ReviewForm(instance=review)

    return render(request, "reviews/edit_review.html", {
        "form": form,
        "review": review,
    })


@login_required
def delete_review(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if review.author != request.user:
        return HttpResponseForbidden("You can't delete this review.")

    puzzle_pk = review.puzzle.pk
    review.delete()
    messages.success(request, "review deleted successfully.")
    return redirect("puzzle_detail", pk=puzzle_pk)
