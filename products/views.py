from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from .models import Products, Categories
from .forms import ProductsForm

# Create your views here.


def all_products(request):
    """ a view to show all products, including sorting and search queries"""
    products = Products.objects.all()

    query = None
    categories = None
    platforms = None
    sort = None
    direction = None

    if request.GET:

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Categories.objects.filter(name__in=categories)

        if 'platform' in request.GET:
            platforms = request.GET['platform'].split(',')
            products = products.filter(platform__in=platforms)
            platforms = Products.objects.filter(name__in=platforms)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter a serach")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'platform': platforms,
        'current_categories': categories,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ a view to show single products """
    product = get_object_or_404(Products, pk=product_id)

    context = {
        'product': product
    }

    return render(request, 'products/product_detail.html', context)


def add_product(request):
    """for superusers to add products to the store """

    if request.method == 'POST':
        form = ProductsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product was successfully added!')
            return redirect(reverse('add_products'))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form was completed correctly.')
    else:
        form = ProductsForm()

    form = ProductsForm()
    template = 'products/add_products.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_product(request, product_id):
    """for superusers to edit products in the store """
    product = get_object_or_404(Products, pk=product_id)
    if request.method == 'POST':
        form = ProductsForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully edited product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to edit product. Please ensure the form is valid.')
    else:
        form = ProductsForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_products.html'
    context = {
        'form': form,
        'product': product
    }

    return render(request, template, context)
