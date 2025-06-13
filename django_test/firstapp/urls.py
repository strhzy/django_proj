from django.contrib import admin
from django.urls import path

from .views import home,cart,catalog,about

urlpatterns = [
    path('', home, name='home'),
    path('catalog/', catalog, name='catalog'),
    path('cart/', cart, name='cart'),
    path('<int:product_id>/', about, name='about'),
]