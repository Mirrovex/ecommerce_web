from django.urls import path

from .views import *


urlpatterns = [
    path('shipping', shipping, name='shipping'),
	path('success', pay_success, name='pay_success'),
]
