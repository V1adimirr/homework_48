from django import forms
from Product.models import Products


class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['product', 'description', 'category', 'remainder', 'price']


class SearchForm(forms.Form):
    search = forms.CharField(max_length=30, required=False, label="")
