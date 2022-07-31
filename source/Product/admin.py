from django.contrib import admin
from Product.models import Products, Basket


class ProductsAdmin(admin.ModelAdmin):
    list_display = ['product', 'category', 'remainder', 'price']
    list_filter = ['category']
    search_fields = ['category']
    fields = ['product', 'description', 'category', 'remainder', 'price']


admin.site.register(Products, ProductsAdmin)


class BasketAdmin(admin.ModelAdmin):
    list_display = ['item', 'count']
    list_filter = ['count']
    search_fields = ['item']
    fields = ['item', 'count']


admin.site.register(Basket, BasketAdmin)
