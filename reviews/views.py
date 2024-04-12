from django.shortcuts import render, redirect
from .forms import ReviewForm
from .models import Review

def customer_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('review') 
    else:
        form = ReviewForm()
    return render(request, 'review.html', {'form': form})


def review_list(request):
    reviews = Review.objects.all()
    return render(request, 'review.html', {'reviews': reviews})