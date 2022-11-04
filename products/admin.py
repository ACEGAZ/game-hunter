from django.contrib import admin
from .models import Categories, Products
# Register your models here.


class CategoriesAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


class ProductsAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'platform',
        'price',
        'image',
    )


admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Products, ProductsAdmin)
