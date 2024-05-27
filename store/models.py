from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cart = models.CharField(max_length=200, blank=True, null=True)

    phone = models.CharField(max_length=20, blank=True)
    address1 = models.CharField(max_length=100, blank=True)
    address2 = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    zipcode = models.CharField(max_length=100, blank=True)

    date_modified = models.DateTimeField(User, auto_now=True)

    def __str__(self):
        return str(self.user)
    

def create_customer(sender, instance, created, **kwargs):
    if created:
        customer = Customer(user=instance)
        customer.save()

post_save.connect(create_customer, sender=User)


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=300, blank=True, null=True)
    image = models.ImageField(upload_to='products/', blank=True)

    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0, decimal_places=2, max_digits=6)

    def __str__(self):
        return self.name


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    date = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.customer.user