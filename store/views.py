from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django import forms

from .models import Product
from .forms import SignupForm


def home(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def about(request):
    return render(request, 'about.html', {})


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
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
                return redirect('home')
            
        messages.error(request, "There was a problem with registering")

    return render(request, 'register.html', {'form': form})