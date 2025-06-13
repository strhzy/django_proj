from django import forms
from .models import Category, Manufacturer, Product, Customer, Review, Order, OrderItem, CartItem

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

class ManufacturerForm(forms.ModelForm):
    class Meta:
        model = Manufacturer
        fields = ['name', 'country', 'website']
        widgets = {
            'website': forms.URLInput(attrs={'placeholder': 'https://example.com'}),
        }

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'photo', 'is_exists', 'manufacturer', 'category']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'photo': forms.FileInput(),
            'price': forms.NumberInput(attrs={'step': '0.01'}),
        }

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'email', 'phone', 'address']
        widgets = {
            'address': forms.Textarea(attrs={'rows': 4}),
            'email': forms.EmailInput(),
        }

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['product', 'customer', 'rating', 'comment']
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 4}),
            'rating': forms.Select(choices=[(i, str(i)) for i in range(1, 6)]),
        }

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer', 'status', 'total_price']
        widgets = {
            'total_price': forms.NumberInput(attrs={'step': '0.01'}),
            'status': forms.Select(),
        }

class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['order', 'product', 'quantity', 'price']
        widgets = {
            'price': forms.NumberInput(attrs={'step': '0.01'}),
            'quantity': forms.NumberInput(attrs={'min': 1}),
        }

class CartItemForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = ['user', 'product', 'quantity', 'price']
        widgets = {
            'price': forms.NumberInput(attrs={'step': '0.01'}),
            'quantity': forms.NumberInput(attrs={'min': 1}),
        }