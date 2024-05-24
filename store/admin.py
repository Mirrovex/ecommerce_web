from django.contrib import admin

from .models import *


admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Product)

class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'product', 'date']
admin.site.register(Order, OrderAdmin)