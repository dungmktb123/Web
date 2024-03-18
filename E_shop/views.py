from django.shortcuts import render, redirect
from store_app.models import Product

def BASE(request):
    return render(request, 'Main/base.html')


def HOME(request):
    product = Product.objects.filter(status='Publish')

    context = {
        'product': product,
    }
    return render(request, "Main/index.html", context)


def PRODUCT(request):
    product = Product.objects.filter(status='P')
    return render(request, "Main/product.html")