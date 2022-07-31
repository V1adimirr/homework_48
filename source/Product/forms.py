from django import forms
from django.forms import widgets
from Product.models import Products


class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['product', 'description', 'category', 'remainder', 'price']
