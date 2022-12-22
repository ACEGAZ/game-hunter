from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from products.models import Products

# Create your views here.


def bag_view(request):
    """ a view to return the bag page"""

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """add item quantity to bag"""

    product = get_object_or_404(Products, pk=item_id)
    bag = request.session.get('bag', {})
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(request, f'added {product.name} to your loot')
    else:
        bag[item_id] = quantity
        messages.success(request, f'added {product.name} to your loot')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """
    Adjust the quantity of the specified product
    """
    product = get_object_or_404(Products, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(request, f'Updated {product.name} quantity \
                         to {bag[item_id]}')
    else:
        bag.pop(item_id)
        messages.success(request, f'Removed {product.name} from your bag')

    request.session['bag'] = bag
    return redirect(reverse('bag_view'))


def remove_from_bag(request, item_id):
    """
    remove the quantity of the specified product
    """
    product = get_object_or_404(Products, pk=item_id)
    bag = request.session.get('bag', {})
    quantity = bag[item_id] - 99

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(request, f'removed {product.name} from your loot')
    else:
        bag.pop(item_id)
        messages.success(request, f'removed {product.name} from your loot')
    if not bag:
        return redirect(reverse('bag_view'))
    return redirect(reverse('bag_view'))
