from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category, Manufacturer

# Create your views here.
def home(request):
    return render(request, 'home.html')

def cart(request):
    return render(request, 'cart.html')

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
    return render(request, 'catalog.html', context)

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
    return render(request, 'about.html', {'product': product})