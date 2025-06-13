from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Category, Manufacturer, Product, Customer, Review, Order, OrderItem, CartItem
from .forms import CategoryForm, ManufacturerForm, ProductForm, CustomerForm, ReviewForm, OrderForm, OrderItemForm, CartItemForm

# Category Views
class CategoryListView(ListView):
    model = Category
    template_name = 'forms/category/category_list.html'
    context_object_name = 'categories'

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'forms/category/category_detail.html'

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'forms/category/category_form.html'
    success_url = reverse_lazy('firstapp:category_list')

class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'forms/category/category_form.html'
    success_url = reverse_lazy('firstapp:category_list')

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'forms/category/category_confirm_delete.html'
    success_url = reverse_lazy('firstapp:category_list')

# Manufacturer Views
class ManufacturerListView(ListView):
    model = Manufacturer
    template_name = 'forms/manufacturer/manufacturer_list.html'
    context_object_name = 'manufacturers'

class ManufacturerDetailView(DetailView):
    model = Manufacturer
    template_name = 'forms/manufacturer/manufacturer_detail.html'

class ManufacturerCreateView(CreateView):
    model = Manufacturer
    form_class = ManufacturerForm
    template_name = 'forms/manufacturer/manufacturer_form.html'
    success_url = reverse_lazy('firstapp:manufacturer_list')

class ManufacturerUpdateView(UpdateView):
    model = Manufacturer
    form_class = ManufacturerForm
    template_name = 'forms/manufacturer/manufacturer_form.html'
    success_url = reverse_lazy('firstapp:manufacturer_list')

class ManufacturerDeleteView(DeleteView):
    model = Manufacturer
    template_name = 'forms/manufacturer/manufacturer_confirm_delete.html'
    success_url = reverse_lazy('firstapp:manufacturer_list')

# Product Views
class ProductListView(ListView):
    model = Product
    template_name = 'forms/product/product_list.html'
    context_object_name = 'products'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'forms/product/product_detail.html'

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'forms/product/product_form.html'
    success_url = reverse_lazy('firstapp:product_list')

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'forms/product/product_form.html'
    success_url = reverse_lazy('firstapp:product_list')

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'forms/product/product_confirm_delete.html'
    success_url = reverse_lazy('firstapp:product_list')

# Customer Views
class CustomerListView(ListView):
    model = Customer
    template_name = 'forms/customer/customer_list.html'
    context_object_name = 'customers'

class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'forms/customer/customer_detail.html'

class CustomerCreateView(CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'forms/customer/customer_form.html'
    success_url = reverse_lazy('firstapp:customer_list')

class CustomerUpdateView(UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'forms/customer/customer_form.html'
    success_url = reverse_lazy('firstapp:customer_list')

class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'forms/customer/customer_confirm_delete.html'
    success_url = reverse_lazy('firstapp:customer_list')

# Review Views
class ReviewListView(ListView):
    model = Review
    template_name = 'forms/review/review_list.html'
    context_object_name = 'reviews'

class ReviewDetailView(DetailView):
    model = Review
    template_name = 'forms/review/review_detail.html'

class ReviewCreateView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'forms/review/review_form.html'
    success_url = reverse_lazy('firstapp:review_list')

class ReviewUpdateView(UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = 'forms/review/review_form.html'
    success_url = reverse_lazy('firstapp:review_list')

class ReviewDeleteView(DeleteView):
    model = Review
    template_name = 'forms/review/review_confirm_delete.html'
    success_url = reverse_lazy('firstapp:review_list')

# Order Views
class OrderListView(ListView):
    model = Order
    template_name = 'forms/order/order_list.html'
    context_object_name = 'orders'

class OrderDetailView(DetailView):
    model = Order
    template_name = 'forms/order/order_detail.html'

class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'forms/order/order_form.html'
    success_url = reverse_lazy('firstapp:order_list')

class OrderUpdateView(UpdateView):
    model = Order
    form_class = OrderForm
    template_name = 'forms/order/order_form.html'
    success_url = reverse_lazy('firstapp:order_list')

class OrderDeleteView(DeleteView):
    model = Order
    template_name = 'forms/order/order_confirm_delete.html'
    success_url = reverse_lazy('firstapp:order_list')

# OrderItem Views
class OrderItemListView(ListView):
    model = OrderItem
    template_name = 'forms/orderitem/orderitem_list.html'
    context_object_name = 'order_items'

class OrderItemDetailView(DetailView):
    model = OrderItem
    template_name = 'forms/orderitem/orderitem_detail.html'

class OrderItemCreateView(CreateView):
    model = OrderItem
    form_class = OrderItemForm
    template_name = 'forms/orderitem/orderitem_form.html'
    success_url = reverse_lazy('firstapp:orderitem_list')

class OrderItemUpdateView(UpdateView):
    model = OrderItem
    form_class = OrderItemForm
    template_name = 'forms/orderitem/orderitem_form.html'
    success_url = reverse_lazy('firstapp:orderitem_list')

class OrderItemDeleteView(DeleteView):
    model = OrderItem
    template_name = 'forms/orderitem/orderitem_confirm_delete.html'
    success_url = reverse_lazy('firstapp:orderitem_list')

# CartItem Views
class CartItemListView(ListView):
    model = CartItem
    template_name = 'forms/cartitem/cartitem_list.html'
    context_object_name = 'cart_items'

class CartItemDetailView(DetailView):
    model = CartItem
    template_name = 'forms/cartitem/cartitem_detail.html'

class CartItemCreateView(CreateView):
    model = CartItem
    form_class = CartItemForm
    template_name = 'forms/cartitem/cartitem_form.html'
    success_url = reverse_lazy('firstapp:cartitem_list')

class CartItemUpdateView(UpdateView):
    model = CartItem
    form_class = CartItemForm
    template_name = 'forms/cartitem/cartitem_form.html'
    success_url = reverse_lazy('firstapp:cartitem_list')

class CartItemDeleteView(DeleteView):
    model = CartItem
    template_name = 'forms/cartitem/cartitem_confirm_delete.html'
    success_url = reverse_lazy('firstapp:cartitem_list')

# Create your views here.
def home(request):
    return render(request, 'firstapp/home.html')

def cart(request):
    return render(request, 'firstapp/cart.html')

def catalog(request):
    products = Product.objects.filter(is_exists=True)

    category_id = request.GET.get('category')
    if category_id:
        products = products.filter(category_id=category_id)

    manufacturer_id = request.GET.get('manufacturer')
    if manufacturer_id:
        products = products.filter(manufacturer_id=manufacturer_id)

    search_query = request.GET.get('search')
    if search_query:
        products = products.filter(name__icontains=search_query) | products.filter(description__icontains=search_query)

    sort = request.GET.get('sort')
    if sort == 'price_asc':
        products = products.order_by('price')
    elif sort == 'price_desc':
        products = products.order_by('-price')

    categories = Category.objects.all()
    manufacturers = Manufacturer.objects.all()
    
    context = {
        'products': products,
        'categories': categories,
        'manufacturers': manufacturers,
        'sort': sort or '',
        'category': category_id or '',
        'manufacturer': manufacturer_id or '',
        'search': search_query or '',
    }
    return render(request, 'firstapp/catalog.html', context)

def about(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST' and request.user.is_authenticated:
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')
        try:
            customer = Customer.objects.get(email=request.user.email)
            Review.objects.create(
                product=product,
                customer=customer,
                rating=rating,
                comment=comment
            )
            messages.success(request, "Отзыв добавлен! 😎")
        except Customer.DoesNotExist:
            messages.error(request, "Создайте профиль клиента с этим email.")
        return redirect('about', product_id=product_id)
    return render(request, 'firstapp/about.html', {'product': product})