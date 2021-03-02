from django.contrib import admin

from django.contrib import admin
from products.models import *

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    model = Product
    # readonly_fields = ["user", "sales", "price", "avialable", "deleted"]
    list_display = ["id", "name", "user", "price", "category" , "available", "deleted"]
    list_display_links = ("id", "name", "user")
    list_editable = ("price",)
    search_fields = ["name", "description", "user__username"]
    list_filter = ["category", "name"]
    list_per_page = 10


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = [ "name" , "description" ]
    search_fields = ["name", "product__name"]