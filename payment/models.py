from django.db import models
from django.contrib.auth.models import User

from store.models import Product


class Shipping(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    full_name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100, blank=True, null=True)
    zipcode = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self) -> str:
        return self.full_name
    

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    full_name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    address = models.TextField(max_length=1000)
    amount_paid = models.DecimalField(max_digits=6, decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'Order - {self.id}'


class OrderItems(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self) -> str:
        return f'order Item - {self.id}'