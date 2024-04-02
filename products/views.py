from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Product, Category
from django.contrib import messages

def all_products(request):
    products = Product.objects.all()
    categories = Category.objects.filter(is_active=True)
    sort = None
    direction = None
    query = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)
            
        if 'category' in request.GET:
            categories = request.GET.getlist('category')  
            products = products.filter(category__id__in=categories)
            categories = Category.objects.filter(id__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products.html', context, {'products': products, 'categories': categories})



def all_categories(request):
    categories = Category.objects.filter(is_active=True)
    return render(request, 'all_categories.html', {'categories': categories})


def main_category(request, category_id):
    category = Category.objects.get(id=category_id)
    products = category.products.all()
    subcategories = category.subcategories.all()

    return render(request, 'category.html', {'category': category, 'products': products, 'subcategories': subcategories})


def subcategory_view(request, subcategory_id):
    subcategory = Subcategory.objects.get(id=subcategory_id)
    products = subcategory.products.all()
    
    return render(request, 'sub_category.html', {'subcategory': subcategory, 'products': products})