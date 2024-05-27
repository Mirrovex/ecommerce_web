from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import ShippingForm
from .models import Shipping


def pay_success(request):
    return render(request, 'pay_success.html', {})


def shipping(request):
    if request.user.is_authenticated:
        shipping = Shipping.objects.get(user=request.user)
        form = ShippingForm(request.POST or None, instance=shipping)

        if form.is_valid():
            form.save()

            messages.success(request, "Shipping has been updated")
            return redirect('shipping')
            
        return render(request, 'shipping.html', {'form': form})
    
    messages.error(request, "You must be logged in to access this page")
    return redirect('home')