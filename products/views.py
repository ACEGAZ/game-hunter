from django.shortcuts import render, get_object_or_404
from .models import Products

# Create your views here.


def all_products(request):
    """ a view to show all products, including sorting and search queries"""
    products = Products.objects.all()

    context = {
        'products': products
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ a view to show single products """
    product = get_object_or_404(Products, pk=product_id)

    context = {
        'product': product
    }

    return render(request, 'products/product_detail.html', context)
