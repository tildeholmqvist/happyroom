from .models import Review 

def reviews_context(request):

    reviews = Review.objects.all()

    return {'reviews': reviews}