from django.shortcuts import render

# Create your views here.
def index(request):
    comments = {}
    return render(request, "index.html", comments)


def cart(request):
    comments = {}
    return render(request, "cart.html", comments)
