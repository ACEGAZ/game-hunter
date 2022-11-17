from django.contrib import admin
from .models import Order, OrderItem
# Register your models here.


class OrderItemAdminInline(admin.TabularInline):
    model = OrderItem
    readonly_fields = ('order_item_total',)


class OrderAdmin(admin.ModelAdmin):

    inlines = (OrderItemAdminInline,)

    list_display = (
        'order_number',
        'first_name',
        'last_name',
        'email',
        'phone_number',
        'street_address_1',
        'street_address_2',
        'county',
        'town_or_city',
        'post_code',
        'date',
        'order_total',
    )

    fields = (
        'order_number',
        'first_name',
        'last_name',
        'email',
        'phone_number',
        'street_address_1',
        'street_address_2',
        'county',
        'town_or_city',
        'post_code',
        'date',
        'order_total',
    )

    readonly_fields = ('order_number', 'date',
                       'order_total',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
