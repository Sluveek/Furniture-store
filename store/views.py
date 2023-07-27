from django.shortcuts import render
from .models import Product

# Create your views here.

# Create your views here.
def index(request):
    products = Product.objects.all()
    comments = {"products":products}
    return render(request, "index.html", comments)


def cart(request):
    comments = {}
    return render(request, "cart.html", comments)
