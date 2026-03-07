from django.shortcuts import render
from .models import Product

# Create your views here.
def product(request):
    return render(request, 'products/product.html')


def products(request):
    pro = Product.objects.all()
    # X = {'pro' : pro}
    # X = {'pro' : pro.filter(price = 15)}
    # X = {'pro' : pro.order_by('name')}
    # X = {'pro' : pro.count()}
    # X = {'pro' : pro.exclude(price=15)}
    # X = {'pro' : pro.filter(price__exact = 15)}
    # X = {'pro' : pro.filter(price__in = [15,25])}
    X = {'pro' : pro.filter(price__range = (10,100))}
    return render(request, 'products/products.html', X)
    # return render(request, 'products/products.html', {'pro' : Product.objects.get(id = 3)})

