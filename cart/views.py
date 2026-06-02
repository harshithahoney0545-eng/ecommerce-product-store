from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart
from products.models import Product


def add_to_cart(request, id):
    if not request.user.is_authenticated:
        return redirect('login')

    product = get_object_or_404(Product, id=id)

    cart_item, created = Cart.objects.get_or_create(
        user=request.user,
        product=product
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('home')


def cart_view(request):
    if not request.user.is_authenticated:
        return redirect('login')

    cart_items = Cart.objects.filter(user=request.user)

    total = 0
    for item in cart_items:
        total += item.product.price * item.quantity

    context = {
        'cart_items': cart_items,
        'total': total
    }

    return render(request, 'cart/cart.html', context)


def remove_from_cart(request, id):
    cart_item = get_object_or_404(Cart, id=id)

    if cart_item.user == request.user:
        cart_item.delete()

    return redirect('cart')