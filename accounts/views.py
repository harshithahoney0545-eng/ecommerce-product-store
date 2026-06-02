from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


# LOGIN VIEW
def login_view(request):
    return render(request, 'accounts/login.html')


# SIGNUP VIEW
def signup_view(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # check user exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('signup')

        # create user
        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        messages.success(request, 'Account created successfully')
        return redirect('login')

    return render(request, 'accounts/signup.html')


# PROFILE VIEW (LOGIN REQUIRED)
@login_required
def profile(request):
    return render(request, 'profile.html')


# LOGOUT VIEW
def logout_view(request):
    logout(request)
    return redirect('signup')


# CART VIEW
def cart_view(request):
    return render(request, 'cart/cart.html')