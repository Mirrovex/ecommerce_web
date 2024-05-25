from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from store.models import Product
from .cart import Cart


def cart(request):
    cart = Cart(request)
    products = cart.get_products()
    quantities = cart.get_quantities()
    return render(request, 'cart.html', {'products': products, 'quantities': quantities})


def cart_add(request):
    cart = Cart(request)

    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        quantity = int(request.POST.get('quantity'))
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product, quantity=quantity)

        cart_quantity = cart.__len__()

        return JsonResponse({'quantity' : cart_quantity})


def cart_delete(request):
    pass


def cart_update(request):
    pass