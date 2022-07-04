from django.urls import path
from Product.views import index_view, product_view

urlpatterns = [
    path('', index_view, name="index"),
    path('product/<int:pk>/view/', product_view, name='product_view')
]