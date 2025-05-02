from django.db import models

class MenuItem(models.Model):
    CATEGORY_CHOICES = [('food', 'Food'), ('drink', 'Drink')]

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    is_special = models.BooleanField(default=False)

    def __str__(self):
        return self.name
