from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages

from store.models import Product
from .cart import Cart


def cart(request):
    cart = Cart(request)
    products = cart.get_products()
    quantities = cart.get_quantities()
    total = cart.total()
    return render(request, 'cart.html', {'products': products, 'quantities': quantities, 'total': total})


def cart_add(request):
    cart = Cart(request)

    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        quantity = int(request.POST.get('quantity'))
        product = get_object_or_404(Product, id=product_id)
        cart.add(product_id, quantity)

        cart_quantity = cart.__len__()

        messages.success(request, "Product added to cart")
        return JsonResponse({'quantity' : cart_quantity})


def cart_delete(request):
    cart = Cart(request)

    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))

        cart.delete(product_id=product_id)

        messages.success(request, "Product deleted from cart")
        return JsonResponse({'product_id': product_id})


def cart_update(request):
    cart = Cart(request)

    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        quantity = int(request.POST.get('quantity'))

        cart.update(product_id=product_id, quantity=quantity)

        return JsonResponse({'quantity': quantity})