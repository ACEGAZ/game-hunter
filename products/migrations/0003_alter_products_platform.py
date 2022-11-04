# Generated by Django 4.1.2 on 2022-11-04 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_products_platform'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='platform',
            field=models.CharField(choices=[('PS4', 'PS4'), ('PS5', 'PS5'), ('XBOX 360', 'XBOX 360'), ('XBOX SERIES X', 'XBOX SERIES X'), ('SWITCH', 'SWITCH')], max_length=254, null=True),
        ),
    ]
