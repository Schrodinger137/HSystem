from django.db.models.signals import post_save
from django.dispatch import receiver
from sales.models import Sale
from .models import Expense, FinancialRecord

@receiver(post_save, sender=Sale)
def create_fin_record_for_sale(sender, instance, created, **kwargs):
    if created:
        FinancialRecord.objects.create(sale=instance)

@receiver(post_save, sender=Expense)
def create_fin_record_for_expense(sender, instance, created, **kwargs):
    if created:
        FinancialRecord.objects.create(expense=instance)
