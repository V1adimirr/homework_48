from django.shortcuts import render, get_object_or_404, redirect

from Product.models import Products


def index_view(request):
    product = Products.objects.all()
    context = {"products": product}
    return render(request, "index.html", context)


def product_view(request, **kwargs):
    product_pk = kwargs.get("pk")
    product = get_object_or_404(Products, pk=product_pk)
    return render(request, 'product_view.html', {"product": product})
