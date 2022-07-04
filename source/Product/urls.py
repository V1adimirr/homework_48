from django.urls import path
from Product.views import index_view, product_view, create_product, delete_product

urlpatterns = [
    path('', index_view, name="index"),
    path('product/create/', create_product, name='create_product'),
    path('product/<int:pk>/view/', product_view, name='product_view'),
    path('product/<int:pk>/delete/', delete_product, name='delete_product')
]