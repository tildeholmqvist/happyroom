from django.shortcuts import render, redirect
from django.urls import reverse
from django.db.models import Q
from .models import Product, Category, News
from django.contrib import messages

def all_products(request):
    """ A view to show all products, including sorting and search queries """
    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

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
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

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

    return render(request, 'products.html', context)



def all_categories(request):
    """ A view to show all categories """
    categories = Category.objects.all()
    selected_category = request.GET.get('category')
    products = None

    if selected_category:
        if selected_category == 'news':
            news_items = News.objects.all()
            context = {
                'categories': categories,
                'selected_category': selected_category,
                'news_items': news_items,
            }
            return render(request, 'all_categories.html', context)
        elif selected_category == 'bestsellers':
            bestsellers = Product.objects.filter(is_bestseller=True)
            context = {
                'categories': categories,
                'selected_category': selected_category,
                'bestsellers': bestsellers,
            }
            return render(request, 'all_categories.html', context)
        else:
            products = Product.objects.filter(category__name=selected_category)
    
    context = {
        'categories': categories,
        'selected_category': selected_category,
        'products': products,
    }
    return render(request, 'all_categories.html', context)
