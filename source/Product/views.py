from django.shortcuts import render, get_object_or_404, redirect

from Product.forms import ProductsForm
from Product.models import Products
from Product.validate import product_validate


def index_view(request):
    product = Products.objects.order_by("product", "category")
    context = {"products": product}
    return render(request, "index.html", context)


def product_view(request, **kwargs):
    product_pk = kwargs.get("pk")
    product = get_object_or_404(Products, pk=product_pk)
    return render(request, 'product_view.html', {"product": product})


def create_product(request):
    if request.method == "GET":
        form = ProductsForm()
        return render(request, "product_create.html", {'form': form})
    else:
        form = ProductsForm(data=request.POST)
        if form.is_valid():
            product = form.cleaned_data.get('product')
            description = form.cleaned_data.get('description')
            category = form.cleaned_data.get('category')
            remainder = form.cleaned_data.get('remainder')
            price = form.cleaned_data.get('price')
            new_entry = Products.objects.create(product=product, description=description, category=category,
                                                remainder=remainder, price=price)
            return redirect("product_view", pk=new_entry.pk)
        return render(request, 'product_create.html', {'form': form})


def delete_product(request, pk):
    entry = get_object_or_404(Products, pk=pk)
    if request.method == "GET":
        return render(request, "delete.html", {"entry": entry})
    else:
        entry.delete()
        return redirect("index")


def update_product(request, pk):
    entry = get_object_or_404(Products, pk=pk)
    if request.method == "GET":
        form = ProductsForm(initial={
            "product": entry.product,
            "description": entry.description,
            "category": entry.category,
            "remainder": entry.remainder,
            "price": entry.price
        })
        return render(request, "update.html", {"form": form})
    else:
        form = ProductsForm(data=request.POST)
        if form.is_valid():
            entry.product = form.cleaned_data.get("product")
            entry.description = form.cleaned_data.get("description")
            entry.category = form.cleaned_data.get("category")
            entry.remainder = form.cleaned_data.get("remainder")
            entry.price = form.cleaned_data.get("price")
            entry.save()
            return redirect("product_view", pk=entry.pk)
        return render(request, "update.html", {"form": form})
