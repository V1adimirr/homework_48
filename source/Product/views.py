from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from Product.forms import ProductsForm
from Product.models import Products


class IndexView(ListView):
    template_name = "index.html"
    model = Products
    context_object_name = 'products'


class ProductView(DetailView):
    template_name = "product_view.html"
    model = Products
    context_object_name = 'product'


class CreateProduct(CreateView):
    form_class = ProductsForm
    template_name = "product_create.html"
    model = Products

    def get_success_url(self):
        return reverse('product_view', kwargs={'pk': self.object.pk})


class DeleteProduct(DeleteView):
    model = Products
    template_name = "delete.html"
    context_object_name = 'entry'

    def get_success_url(self):
        return reverse('index')


class UpdateProduct(UpdateView):
    form_class = ProductsForm
    template_name = "update.html"
    model = Products

    def get_success_url(self):
        return reverse('product_view', kwargs={'pk': self.object.pk})
