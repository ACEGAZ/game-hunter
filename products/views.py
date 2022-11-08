from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from .models import Products, Categories

# Create your views here.


def all_products(request):
    """ a view to show all products, including sorting and search queries"""
    products = Products.objects.all()

    query = None
    categories = None
    platforms = None

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
