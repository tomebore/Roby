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


def category(request, pk):
    context = {}
    category = Category.objects.get(id=pk)
    context["object_list"] = Product.objects.filter(
        category==category,
        deleted=False
    )
    context["category_pk"] = pk
    return render(request, "product/products.html", context)
