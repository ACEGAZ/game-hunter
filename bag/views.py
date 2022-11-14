from django.shortcuts import render, redirect, reverse
# Create your views here.


def bag_view(request):
    """ a view to return the bag page"""

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """add item quantity to bag"""

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """
    Adjust the quantity of the specified product to the specified
    amount

    url for this function should be <str:id> not <int:id>
    - otherwise you need to add str() method for each dict representation.
    """
    bag = request.session.get('bag', {})
    quantity = bag[item_id] - 1

    if quantity > 0:
        bag[item_id] = quantity
    else:
        bag.pop(item_id)
    request.session['bag'] = bag
    if not bag:
        return redirect(reverse('bag_view'))
    return redirect(reverse('bag_view'))
