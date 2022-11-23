import uuid
from django.db import models
from django.db.models import Sum
from django.conf import settings
from products.models import Products


class Order(models.Model):
    order_number = models.CharField(null=False, editable=False, max_length=32)
    first_name = models.CharField(null=False, blank=False, max_length=50)
    last_name = models.CharField(null=False, blank=False, max_length=50)
    email = models.EmailField(blank=False, null=False, max_length=254)
    phone_number = models.CharField(blank=False, null=False,
                                    max_length=20)
    street_address_1 = models.CharField(blank=False, null=False, max_length=80)
    street_address_2 = models.CharField(blank=True, null=True, max_length=80)
    county = models.CharField(blank=False, null=False, max_length=40)
    town_or_city = models.CharField(blank=False, null=False, max_length=40)
    post_code = models.CharField(blank=False, null=False, max_length=20)
    date = models.DateTimeField(auto_now_add=True)
    order_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=False, default=0)

    def _generate_order_number(self):
        """ generate unique order number using UUID """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update grand total each time a line item is added.
        """
        self.order_total = self.order_items.aggregate(Sum('order_item_total'))['order_item_total__sum'] or 0
        self.order_total
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number

    class Meta:
        verbose_name_plural = 'Orders'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, blank=False, null=False,
                              on_delete=models.CASCADE,
                              related_name='order_items')
    product = models.ForeignKey(Products, blank=False, null=False,
                                on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    order_item_total = models.DecimalField(max_digits=6, decimal_places=2,
                                           blank=False, null=False,
                                           editable=False)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """
        self.order_item_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.order.order_number}'

    class Meta:
        verbose_name_plural = 'Order Items'
