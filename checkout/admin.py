from django.contrib import admin
from .models import Order, OrderItem, Feedback
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
        'user_profile',
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
        'original_bag',
        'stripe_pid',
    )

    readonly_fields = ('order_number',
                       'date',
                       'order_total',
                       'original_bag',
                       'stripe_pid',
                       )

    ordering = ('-date',)


class FeedbackAdmin(admin.ModelAdmin):
    model = Feedback

    fields = (
        'delivery_time',
        'website',
        'checkout',
    )

    list_display = (
        'delivery_time',
        'website',
        'checkout',
    )

    readonly_fields = (
        'delivery_time',
        'website',
        'checkout',
    )

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
admin.site.register(Feedback, FeedbackAdmin)
