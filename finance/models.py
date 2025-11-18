from django.db import models
from sales.models import *
# Create your models here.
class Expense(models.Model):
    name = models.CharField(max_length=150)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

class FinancialRecord(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, null=True, blank=True)
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
