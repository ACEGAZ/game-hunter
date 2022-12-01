from django import forms
from .models import Products, Categories


class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = '__all__'
