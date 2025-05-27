from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer_name', 'customer_address', 'ordered_books', 'ordered_menu_items']
        widgets = {
            'ordered_books': forms.CheckboxSelectMultiple,
            'ordered_menu_items': forms.CheckboxSelectMultiple,
        }