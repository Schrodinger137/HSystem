from django.db import models
from products.models import *

# Create your models here.
class Sale(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    order_type = models.CharField(max_length=20)

class SaleItem(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
