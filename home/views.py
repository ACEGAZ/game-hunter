from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from .models import Reviews
from .forms import ReviewsForm

# Create your views here.


def index(request):
    """ a view to return the index page"""
    review = Reviews.objects.all()
    last_eight_reviews = Reviews.objects.all().order_by('-id')[:8][::-1]
    context = {
        'last_eight_reviews': last_eight_reviews,
        'review': review
    }
    return render(request, 'home/index.html', context)


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
            return render(request, 'home/add_review_success.html')
        else:
            messages.error(request, 'Failed to add review. Please ensure the form was completed correctly.')
    else:
        form = ReviewsForm()

    form = ReviewsForm()
    context = {
        'form': form,
    }

    return render(request, 'home/add_reviews.html', context)


@login_required
def edit_review(request, review_id):
    """for superusers to edit products in the store """
    if not request.user.is_authenticated:
        messages.error(request, 'Sorry, you need an account to edit a review.')
        return redirect(reverse('home'))

    review = get_object_or_404(Reviews, pk=review_id)
    if request.method == 'POST':
        form = ReviewsForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully edited your review!')
            return redirect(reverse('home'))
        else:
            messages.error(request, 'Failed to edit your review. Please ensure the form is valid.')
    else:
        form = ReviewsForm(instance=review)
        messages.info(request, f'You are editing your review titled {review.title}')

    template = 'home/edit_review.html'
    context = {
        'form': form,
        'review': review
    }

    return render(request, template, context)


@login_required
def delete_review(request, review_id):
    """ Delete a product from the store """
    if not request.user.is_authenticated:
        messages.error(request, 'Sorry, you need an account to delete a review.')
        return redirect(reverse('home'))

    review = get_object_or_404(Reviews, pk=review_id)
    review.delete()
    messages.success(request, 'Review deleted!')
    return redirect(reverse('home'))


def add_review_success(request):
    """ a view to return the add_review_success.html page"""

    return render(request, 'home/add_review_success.html')


@login_required
def delete_review_confirmation(request, review_id):
    """ Render a view to confirm deletion of a product """
    if not request.user.is_authenticated:
        messages.error(request, 'Sorry, you need an account to delete a review.')
        return redirect(reverse('home'))
    review = get_object_or_404(Reviews, pk=review_id)
    template = 'home/delete_review_confirmation.html'
    context = {
        'review': review
    }
    return render(request, template, context)
