from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "amount", "timestamp")
    date_hierarchy = "timestamp"
    search_fields = ("name",)

@admin.register(FinancialRecord)
class FinancialRecordAdmin(admin.ModelAdmin):
    list_display = ("id", "sale", "expense", "created_at")
    list_filter = ("created_at",)
    date_hierarchy = "created_at"