from django.contrib import admin
from .models import Order, OrderItem
# Register your models here.


class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'order_number',
        'first_name',
        'last_name',
        'email',
        'phone_number',
        'street_address_1',
        'street_address_2',
        'order_number',
        'county',
        'town_or_city',
        'post_code',
        'date',
        'order_total',
    )


class OrderItemAdmin(admin.ModelAdmin):
    list_display = (
        'order',
        'product',
        'qauntity',
        'order_item_total',
    )


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
