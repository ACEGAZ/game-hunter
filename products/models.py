from django.db import models

# Create your models here.

PS4 = 'PS4'
PS5 = 'PS5'
XBOX_ONE = 'XBOX ONE'
XBOX_SERIES_X = 'XBOX SERIES X'
SWITCH = 'SWITCH'


class Categories(models.Model):
    name = models.CharField(max_length=254)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Products(models.Model):
    PLATFORM_CHOICES = (
                       (PS4, "PS4"),
                       (PS5, "PS5"),
                       (XBOX_ONE, "XBOX ONE"),
                       (XBOX_SERIES_X, "XBOX SERIES X"),
                       (SWITCH, "SWITCH"),
                       )

    class Meta:
        verbose_name_plural = 'Products'

    category = models.ForeignKey('Categories', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    platform = models.CharField(max_length=254, null=True,
                                choices=PLATFORM_CHOICES)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
