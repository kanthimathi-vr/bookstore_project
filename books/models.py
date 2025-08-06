

# Create your models here.
from django.db import models
from decimal import Decimal

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    discount_percent = models.PositiveIntegerField(default=0)

    def get_discounted_price(self):
        discount = Decimal(self.discount_percent) / Decimal(100)
        return self.price * (Decimal('1.0') - discount)
    def __str__(self):
        return self.title
