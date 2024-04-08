from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower 
from .models import Product, Category, SubCategory
from django.contrib import messages
from .forms import ProductForm
from services.forms import ServiceForm



def all_products(request):
    """ A view to show all products, including sorting and search queries """
    products = Product.objects.all()
    query = None
    categories = None
    sub_categories = None
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
            categories = request.GET.getlist('category')  
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'sub_category' in request.GET:
            sub_categories = request.GET.getlist('sub_category')  
            products = products.filter(sub_category__name__in=sub_categories)
            sub_categories = SubCategory.objects.filter(name__in=sub_categories)

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
        'current_sub_categories': sub_categories,  
    }

    return render(request, 'products.html', context)


# from walkthrough
def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'product_detail.html', context)


def bestsellers(request):
    bestsellers = Product.objects.filter(is_bestseller=True)
    context = {
        'products': bestsellers,
        'selected_category': 'bestsellers',
    }
    return render(request, 'all_categories.html', context)


def new_items(request):
    new_items = Product.objects.filter(is_new_items=True)
    context = {
        'products': new_items,
        'selected_category': 'new_items',
    }
    return render(request, 'all_categories.html', context)


def last_chance(request):
    last_chance = Product.objects.filter(is_last_chance=True)
    context = {
        'products': last_chance,
        'selected_category': 'last_chance',
    }
    return render(request, 'all_categories.html', context)


def all_categories(request):
    """ A view to show all categories or subcategories """
    categories = Category.objects.all()
    selected_category = request.GET.get('category')
    selected_subcategory = request.GET.get('sub_category')
    products = None
    sub_category_products = None

    if selected_subcategory:
        products = Product.objects.filter(sub_category__name=selected_subcategory)
    elif selected_category:
        products = Product.objects.filter(category__name=selected_category)

    selected_category_friendly_name = Category.objects.get(name=selected_category).friendly_name if selected_category else None
    selected_subcategory_friendly_name = SubCategory.objects.get(name=selected_subcategory).friendly_name if selected_subcategory else None

    context = {
        'categories': categories,
        'selected_category': selected_category,
        'selected_category_friendly_name': selected_category_friendly_name, 
        'products': products,
        'selected_subcategory': selected_subcategory,
        'selected_subcategory_friendly_name': selected_subcategory_friendly_name, 
    }
    return render(request, 'all_categories.html', context)



def sub_categories(request, category_id):
    """ A view to show subcategories of a specific category """
    category = get_object_or_404(Category, id=category_id)
    subcategories = category.subcategory_set.all()

    products = Product.objects.filter(sub_categories__category=category)

    context = {
        'category': category,
        'subcategories': subcategories,
        'products': products,
    }
    return render(request, 'sub_categories.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product_form = ProductForm(request.POST, request.FILES)
    service_form = ServiceForm(request.POST, request.FILES)

    if request.method == 'POST':
        if 'product_submit' in request.POST:
            if product_form.is_valid():
                product = product_form.save()
                messages.success(request, 'Successfully added product!')
                return redirect(reverse('product_detail', args=[product.id]))
            else:
                messages.error(request, 'Failed to add product, please ensure the form is valid.')
        elif 'service_submit' in request.POST:
            if service_form.is_valid():
                service = service_form.save()
                messages.success(request, 'Successfully added service!')
                return redirect(reverse('service_detail', args=[service.id]))
            else:
                messages.error(request, 'Failed to add service, please ensure the form is valid.')

    template = 'add_product.html'
    context = {
        'product_form': product_form,
        'service_form': service_form,
    }

    return render(request, template, context)



@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure that the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
        
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Successfully deleted product!')
    return redirect(reverse('products'))
