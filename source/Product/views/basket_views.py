from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import DetailView

from Product.forms import BasketForm
from Product.models import Basket, Products


class BasketAdd(DetailView):
    template_name = 'basket/product_add.html'
    form_class = BasketForm
    model = Basket
    context_object_name = 'item'

