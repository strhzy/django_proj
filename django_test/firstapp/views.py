from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def cart(request):
    return render(request, 'cart.html')

def catalog(request):
    return render(request, 'catalog.html')

def about(request):
    return render(request, "about.html")