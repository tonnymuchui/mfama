from django.shortcuts import render
from store.models import Product

def home(request):

    context = {
        'products': products,
    }
    return render(request, 'home.html', context)