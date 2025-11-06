from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseForbidden
from django.db import IntegrityError
from django.views import generic
from .models import Puzzle, TimeSubmission
from .forms import TimeSubmissionForm

# Create your views here.


class Leaderboards(generic.ListView):
    """
    Displays a paginated list of :model:`reviews.Puzzle` entries.

    Each puzzle includes its related :model:`leaderboards.TimeSubmission`
    entries in a table.

    **Context**

    ``puzzles``
        A queryset of :model:`reviews.Puzzle` objects with prefetched times.

    **Template**

    :template:`leaderboards/leaderboards.html`
    """
    model = Puzzle
    template_name = "leaderboards/leaderboards.html"
    context_object_name = "puzzles"
    paginate_by = 5

    def get_queryset(self):
        """
        Prefetch related time submissions for leaderboard display.
        """
        return Puzzle.objects.prefetch_related("times")


def submit_time(request):
    """
    Allows authenticated users to submit a :model:`leaderboards.TimeSubmission`.

    Prevents duplicate submissions per puzzle.

    **Context**

    ``form``
        An instance of :form:`leaderboards.TimeSubmissionForm`.

    **Template**

    :template:`leaderboards/submit_time.html`
    """
    if request.method == "POST":
        form = TimeSubmissionForm(request.POST)
        if form.is_valid():
            time_submission = form.save(commit=False)
            time_submission.user = request.user
            try:
                time_submission.save()
                messages.success(request, "Your time has been submitted!")
                return redirect("leaderboards")
            except IntegrityError:
                messages.error(
                    request,
                    "You can only have one submission for each puzzle. "
                    "Please update your current time instead."
                )

    else:
        form = TimeSubmissionForm()
    return render(request, "leaderboards/submit_time.html", {"form": form})


@login_required
def update_time(request, pk):
    """
    Allows users to update their existing :model:`leaderboards.TimeSubmission`.

    **Context**

    ``form``
        An instance of :form:`leaderboards.TimeSubmissionForm`.
    ``time_submission``
        The :model:`leaderboards.TimeSubmission` being updated.

    **Template**

    :template:`leaderboards/update_time.html`
    """
    time_submission = get_object_or_404(TimeSubmission, pk=pk)
    if time_submission.user != request.user:
        return HttpResponseForbidden("You can't update this time submission.")

    if request.method == "POST":
        form = TimeSubmissionForm(request.POST, instance=time_submission)
        if form.is_valid():
            form.save
            messages.success(request, "Time updated successfully.")
            return redirect("leaderboards")

    else:
        form = TimeSubmissionForm(instance=time_submission)

    return render(request, "leaderboards/update_time.html", {
        "form": form,
        "time_submission": time_submission,
    })


@login_required
def delete_time(request, pk):
    """
    Allow users to delete their :model:`leaderboards.TimeSubmission`.

    Redirects to the leaderboard after deletion.
    """
    time_submission = get_object_or_404(TimeSubmission, pk=pk)
    if time_submission.user != request.user:
        return HttpResponseForbidden("You can't delete this time submission.")

    time_submission.delete()
    messages.success(request, "Time submission deleted successfully.")
    return redirect("leaderboards")
