from django.urls import path

from .views import *


urlpatterns = [
    path('shipping/', shipping, name='shipping'),
    path('checkout/', checkout, name='checkout'),
	path('success/', pay_success, name='pay_success'),
]
