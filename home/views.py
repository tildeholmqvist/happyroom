from django.shortcuts import render
from products.models import Product
from products.views import all_products


# Create your views here.
def index(request):
    return render(request, 'home/index.html')
