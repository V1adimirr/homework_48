from urllib.parse import urlencode

from django.db.models import Q
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from Product.forms import ProductsForm, SearchForm
from Product.models import Products


class IndexView(ListView):
    template_name = "products/index.html"
    model = Products
    context_object_name = 'products'
    ordering = ['-category', '-product']
    paginate_by = 4

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context["form"] = self.form
        if self.search_value:
            query = urlencode({"search": self.search_value})
            context["query"] = query
        return context

    def get_queryset(self):
        if self.search_value:
            return Products.objects.filter(Q(product__icontains=self.search_value))
        return Products.objects.all()

    def get_search_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data.get("search")


class ProductView(DetailView):
    template_name = "products/product_view.html"
    model = Products
    context_object_name = 'product'


class CreateProduct(CreateView):
    form_class = ProductsForm
    template_name = "products/product_create.html"
    model = Products

    def get_success_url(self):
        return reverse('product_view', kwargs={'pk': self.object.pk})


class DeleteProduct(DeleteView):
    model = Products
    template_name = "products/product_delete.html"
    context_object_name = 'entry'

    def get_success_url(self):
        return reverse('index')


class UpdateProduct(UpdateView):
    form_class = ProductsForm
    template_name = "products/product_update.html"
    model = Products

    def get_success_url(self):
        return reverse('product_view', kwargs={'pk': self.object.pk})
