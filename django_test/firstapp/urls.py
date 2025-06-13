from django.contrib import admin
from django.urls import path

from .views import home,cart,catalog,about,CategoryListView, CategoryDetailView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView,ManufacturerListView, ManufacturerDetailView, ManufacturerCreateView, ManufacturerUpdateView, ManufacturerDeleteView,    ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView,     CustomerListView, CustomerDetailView, CustomerCreateView, CustomerUpdateView, CustomerDeleteView,    ReviewListView, ReviewDetailView, ReviewCreateView, ReviewUpdateView, ReviewDeleteView,    OrderListView, OrderDetailView, OrderCreateView, OrderUpdateView, OrderDeleteView,    OrderItemListView, OrderItemDetailView, OrderItemCreateView, OrderItemUpdateView, OrderItemDeleteView, CartItemListView, CartItemDetailView, CartItemCreateView, CartItemUpdateView, CartItemDeleteView

urlpatterns = [
    path('', home, name='home'),
    path('catalog/', catalog, name='catalog'),
    path('cart/', cart, name='cart'),
    path('<int:product_id>/', about, name='about'),
    # Category URLs
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('categories/create/', CategoryCreateView.as_view(), name='category_create'),
    path('categories/<int:pk>/update/', CategoryUpdateView.as_view(), name='category_update'),
    path('categories/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category_delete'),

    # Manufacturer URLs
    path('manufacturers/', ManufacturerListView.as_view(), name='manufacturer_list'),
    path('manufacturers/<int:pk>/', ManufacturerDetailView.as_view(), name='manufacturer_detail'),
    path('manufacturers/create/', ManufacturerCreateView.as_view(), name='manufacturer_create'),
    path('manufacturers/<int:pk>/update/', ManufacturerUpdateView.as_view(), name='manufacturer_update'),
    path('manufacturers/<int:pk>/delete/', ManufacturerDeleteView.as_view(), name='manufacturer_delete'),

    # Product URLs
    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),

    # Customer URLs
    path('customers/', CustomerListView.as_view(), name='customer_list'),
    path('customers/<int:pk>/', CustomerDetailView.as_view(), name='customer_detail'),
    path('customers/create/', CustomerCreateView.as_view(), name='customer_create'),
    path('customers/<int:pk>/update/', CustomerUpdateView.as_view(), name='customer_update'),
    path('customers/<int:pk>/delete/', CustomerDeleteView.as_view(), name='customer_delete'),

    # Review URLs
    path('reviews/', ReviewListView.as_view(), name='review_list'),
    path('reviews/<int:pk>/', ReviewDetailView.as_view(), name='review_detail'),
    path('reviews/create/', ReviewCreateView.as_view(), name='review_create'),
    path('reviews/<int:pk>/update/', ReviewUpdateView.as_view(), name='review_update'),
    path('reviews/<int:pk>/delete/', ReviewDeleteView.as_view(), name='review_delete'),

    # Order URLs
    path('orders/', OrderListView.as_view(), name='order_list'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order_detail'),
    path('orders/create/', OrderCreateView.as_view(), name='order_create'),
    path('orders/<int:pk>/update/', OrderUpdateView.as_view(), name='order_update'),
    path('orders/<int:pk>/delete/', OrderDeleteView.as_view(), name='order_delete'),

    # OrderItem URLs
    path('orderitems/', OrderItemListView.as_view(), name='orderitem_list'),
    path('orderitems/<int:pk>/', OrderItemDetailView.as_view(), name='orderitem_detail'),
    path('orderitems/create/', OrderItemCreateView.as_view(), name='orderitem_create'),
    path('orderitems/<int:pk>/update/', OrderItemUpdateView.as_view(), name='orderitem_update'),
    path('orderitems/<int:pk>/delete/', OrderItemDeleteView.as_view(), name='orderitem_delete'),

    # CartItem URLs
    path('cartitems/', CartItemListView.as_view(), name='cartitem_list'),
    path('cartitems/<int:pk>/', CartItemDetailView.as_view(), name='cartitem_detail'),
    path('cartitems/create/', CartItemCreateView.as_view(), name='cartitem_create'),
    path('cartitems/<int:pk>/update/', CartItemUpdateView.as_view(), name='cartitem_update'),
    path('cartitems/<int:pk>/delete/', CartItemDeleteView.as_view(), name='cartitem_delete'),
]