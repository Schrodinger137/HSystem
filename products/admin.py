from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "precio", "available")
    list_filter = ("available",)
    search_fields = ("name", "description")