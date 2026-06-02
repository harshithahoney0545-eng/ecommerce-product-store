from django.shortcuts import render

def login_view(request):
    return render(request, 'accounts/login.html')

def signup_view(request):
    return render(request, 'accounts/signup.html')

def cart_view(request):
     return render(request, 'cart/cart.html')
    