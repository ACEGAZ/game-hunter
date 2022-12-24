from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from products.models import Products

"""
holds bag items and calculates price
"""


def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        product = get_object_or_404(Products, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    order_total = total

    context = {
        'bag_items': bag_items,
        'total': total,
        'order_total': order_total,
        'product_count': product_count,
    }

    return context
