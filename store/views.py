from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db.models import Q

import json

from .models import Product, Category, Customer
from .forms import SignupForm, UpdateProfile, UpdatePassword
from cart.cart import Cart


def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})


def about(request):
    return render(request, 'about.html', {})


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)

            customer = Customer.objects.get(user=request.user)
            if customer.cart:
                saved_cart = json.loads(customer.cart)
                cart = Cart(request)

                for key, value in saved_cart.items():
                    cart.add(key, value)

            messages.success(request, "You have been logged in")
            return redirect('home')
        
        messages.error(request, "Incorrect Username or Password, try again")

    return render(request, 'login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, "You have been logget out")
    return redirect('home')


def register_user(request):
    form = SignupForm()
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, "Account created, you have been logged in")
                return redirect('update_info')
            
        messages.error(request, "There was a problem with registering")

    return render(request, 'register.html', {'form': form})


def update_user(request):
    if request.user.is_authenticated:
        user = request.user
        form = UpdateProfile(request.POST or None, instance=user)

        if form.is_valid():
            form.save()

            login(request, user)
            messages.success(request, "Profile has been updated")
            return redirect('home')
            
        return render(request, 'update_user.html', {'form': form})
    
    messages.error(request, "You must be logged in to access this page")
    return redirect('home')
    

def update_password(request):
    if request.user.is_authenticated:
        user = request.user
        form = UpdatePassword(user, request.POST or None)

        if form.is_valid():
            form.save()

            login(request, user)
            messages.success(request, "Password has been updated")
            return redirect('update_user')

        return render(request, 'update_password.html', {'form': form})
    
    messages.error(request, "You must be logged in to access this page")
    return redirect('home')


def product(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'product.html', {'product': product})


def category(request, name):
    name = name.replace('-', ' ')
    try:
        category = Category.objects.get(name=name)
        products = Product.objects.filter(category=category)

        return render(request, 'category.html', {'products': products, 'category': category})
    except:
        messages.error(request, "This category doesn't exist")
        return redirect('home')
    
def category_summary(request):
    return render(request, 'category_summary.html', {})


def search(request):
    if request.method == 'POST':
        search = request.POST['search']
        products = Product.objects.filter(Q(name__icontains=search) | Q(description__icontains=search))
        if not products:
            messages.error(request, "Product not found")
        return render(request, "search.html", {'search': search, 'products': products})

    return render(request, "search.html", {})