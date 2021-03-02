from django.shortcuts import render, redirect
from products.models import *
from django.db.models import Q

def products(request):
    context = {}
    context["products"] = Product.objects.filter(
            available=True,
            deleted=False)
    return render(request , "products.html", context)

def product(request,id):
    context = {}
    context["product"] = Product.objects.filter(id=id)
    return render(request ,"product.html" ,context)

