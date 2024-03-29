from django import forms
from django.forms import widgets

from Product.models import Products, Basket


class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['product', 'description', 'category', 'remainder', 'price']


class SearchForm(forms.Form):
    search = forms.CharField(max_length=30, required=False, label="")


class BasketForm(forms.ModelForm):
    class Meta:
        model = Basket
        fields = ['item', 'count']
        widgets = {
            'count': forms.Select,
        }
