from django.contrib import admin
from Product.models import Products


class ProductsAdmin(admin.ModelAdmin):
    list_display = ['product', 'category', 'remainder', 'price']
    list_filter = ['category']
    search_fields = ['category']
    fields = ['product', 'description', 'category', 'remainder', 'price']


admin.site.register(Products, ProductsAdmin)
