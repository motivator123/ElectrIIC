from django.shortcuts import render, get_object_or_404
from .models import Category, Product

def product_list(request, category_slug=None):
    """" Страница списка товаров"""
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    context = {'category': category, 'categories': categories, 'products': products}
    return render(request, 'shop/list.html', context)


def product_detail(request, id, slug):
    """ Страница продукта"""
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    context = {'product': product}
    return render(request, 'shop/detail.html', context)