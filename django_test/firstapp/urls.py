from django.contrib import admin
from django.urls import path

from .views import home,cart,catalog,about

urlpatterns = [
    path('', home),
    path('cart/', cart),
    path('catalog/', catalog),
    path('about/', about),
]
