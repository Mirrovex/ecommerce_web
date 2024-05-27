from django.contrib import admin

from .models import Shipping, Order, OrderItems


admin.site.register(Shipping)
admin.site.register(Order)
admin.site.register(OrderItems)