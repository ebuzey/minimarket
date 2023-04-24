from django.urls import path
from main import api, views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/<str:category_id>/', views.products, name='products'),
    path('product-detail/<int:product_id>', views.product_detail, name='product-detail'),
    path('cart/add/', api.cart_add_product, name='cart_add_product')
]