from django.contrib import admin
from .models import *

# Register your models here.
class SaleItemInline(admin.TabularInline):
    model = SaleItem
    extra = 1

@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ("id", "timestamp", "order_type")
    list_filter = ("order_type", "timestamp")
    date_hierarchy = "timestamp"
    inlines = [SaleItemInline]

@admin.register(SaleItem)
class SaleItemAdmin(admin.ModelAdmin):
    list_display = ("id", "sale", "product", "quantity", "price")
    list_filter = ("product",)
    search_fields = ("product__name",)