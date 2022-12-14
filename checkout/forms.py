from django import forms
from .models import Order, Feedback


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('first_name',
                  'last_name',
                  'email',
                  'phone_number',
                  'street_address_1',
                  'street_address_2',
                  'county',
                  'town_or_city',
                  'post_code')

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'first_name': 'First name',
            'last_name': 'Last name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'post_code': 'Post Code',
            'town_or_city': 'Town or City',
            'street_address_1': 'Street Address 1',
            'street_address_2': 'Street Address 2',
            'county': 'County',
        }

        self.fields['first_name'].widget.attrs['autofocus'] = True
        for field in self.fields:

            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = (
            'delivery_time',
            'website',
            'checkout',)
