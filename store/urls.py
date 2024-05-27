from django.urls import path

from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register_user, name='register'),
    path('update_user/', update_user, name='update_user'),
    # path('update_info/', update_info, name='update_info'),
    path('update_password/', update_password, name='update_password'),
    path('product/<int:id>', product, name='product'),
    path('category/<str:name>', category, name='category'),
    path('category_summary/', category_summary, name='category_summary'),
    path('search/', search, name='search'),
]
