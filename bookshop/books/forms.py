from django import forms
from .models import BookOrder

class BookOrderForm(forms.ModelForm):
    class Meta:
        model = BookOrder
        fields = ['customer_name', 'customer_email', 'book', 'quantity']