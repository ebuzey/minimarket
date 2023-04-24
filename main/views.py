from django.shortcuts import render, get_object_or_404
from .models import Category, Product


def home(request):
    categories = Category.objects.filter(products__available=True).distinct()
    return render(request, 'main/home.html', {'categories': categories})

def products(request, category_id):
    # category = Category.objects.get(id=category_id)
    category = get_object_or_404(Category, id=category_id) # todo: template de 404
    return render(request, 'main/products.html', {'products': category.products.filter(available=True), 'category_name': category.name})

def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'main/product_detail.html', {'product': product})

