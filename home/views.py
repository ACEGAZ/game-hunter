from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Reviews
from .forms import ReviewsForm

# Create your views here.


def index(request):
    """ a view to return the index page"""

    return render(request, 'home/index.html')


@login_required
def add_review(request):
    """ add a review to home page """
    if not request.user.is_authenticated:
        messages.error(request, 'Sorry, you need an account to leave a review.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ReviewsForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.save()
            messages.success(request, 'Thanks for your review')
            return redirect(reverse('home'))
        else:
            messages.error(request, 'Failed to add review. Please ensure the form was completed correctly.')
    else:
        form = ReviewsForm()

    form = ReviewsForm()
    context = {
        'form': form,
    }

    return render(request, 'home/add_reviews.html', context)
