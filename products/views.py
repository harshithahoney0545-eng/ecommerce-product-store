from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Product
import json
import random


def home(request):
    products = Product.objects.all()

    featured_product = Product.objects.order_by('?').first()

    context = {
        'products': products,
        'featured_product': featured_product,
        'product_count': products.count(),
    }

    return render(request, 'products/home.html', context)

# 📦 PRODUCT LIST PAGE
def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})


# ❤️ ADD TO WISHLIST
def add_to_wishlist(request, id):
    if request.method == "POST":
        product = get_object_or_404(Product, id=id)
        print(f"{product.name} added to wishlist")  # temporary

    return redirect('home')


# 🔍 SEARCH FEATURE
def search(request):
    query = request.GET.get('q')

def category_products(request, category_name):
    return render(
        request,
        'products/home.html',
        {'products': Product.objects.all()}
    )

    if query:
        products = Product.objects.filter(name__icontains=query)
    else:
        products = Product.objects.all()

    return render(request, 'products/home.html', {'products': products})


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)

    product.views += 1
    product.save()

    return render(
        request,
        'products/product_detail.html',
        {'product': product}
    )
# 📡 GET ALL PRODUCTS (API)
def api_products(request):
    products = Product.objects.all()

    data = []
    for product in products:
        data.append({
            'id': product.id,
            'name': product.name,
            'price': str(product.price),
        })

    return JsonResponse(data, safe=False)


# ✏️ UPDATE PRODUCT (API)
@csrf_exempt
def api_update_product(request, id):
    if request.method == "PUT":
        product = get_object_or_404(Product, id=id)

        data = json.loads(request.body)

        product.name = data.get('name', product.name)
        product.price = data.get('price', product.price)

        product.save()

        return JsonResponse({'message': 'Product updated successfully'})

    return JsonResponse({'error': 'Invalid request'}, status=400)


# ❌ DELETE PRODUCT (API)
@csrf_exempt
def api_delete_product(request, id):
    if request.method == "DELETE":
        product = get_object_or_404(Product, id=id)
        product.delete()

        return JsonResponse({'message': 'Product deleted successfully'})

    return JsonResponse({'error': 'Invalid request'}, status=400)

def surprise_me(request):
    products = Product.objects.all()

    if products.exists():
        product = random.choice(products)
        return redirect('product_detail', id=product.id)

    return redirect('home')