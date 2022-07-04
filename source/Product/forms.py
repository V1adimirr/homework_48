from django import forms
from Product.models import CATEGORY_CHOICES


class ProductsForm(forms.Form):
    product = forms.CharField(max_length=100, required=True, label='Продукт')
    description = forms.CharField(max_length=2000, required=False, label='Описание')
    category = forms.ChoiceField(required=True, choices=CATEGORY_CHOICES, label='Категория')
    remainder = forms.IntegerField(min_value=0, label='Остаток')
    price = forms.DecimalField(max_digits=7, decimal_places=2, label='Стоимость')
