from django.contrib import admin
from django.contrib.auth.models import User

from .models import *


class CustomerInline(admin.StackedInline):
    model = Customer

class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ['username', 'first_name', 'last_name', 'email']
    inlines = [CustomerInline]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'product', 'date']
admin.site.register(Order, OrderAdmin)


admin.site.register(Category)
admin.site.register(Product)