from django.db import models
from books.models import Book
from menu.models import MenuItem

class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_address = models.TextField()
    ordered_books = models.ManyToManyField(Book, blank=True)
    ordered_menu_items = models.ManyToManyField(MenuItem, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order by {self.customer_name}"