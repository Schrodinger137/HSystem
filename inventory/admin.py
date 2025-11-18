from django.contrib import admin
from .models import * 

# Register your models here.

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "unit", "cost_per_unit", "stock_actual")
    search_fields = ("name",)

    def stock_actual(self, obj):
        return obj.stock_actual()

    stock_actual.short_description = "Stock Actual"

class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 1

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ("id", "product")
    search_fields = ("product__name",)
    inlines = [RecipeIngredientInline]

@admin.register(RecipeIngredient)
class RecipeIngredientAdmin(admin.ModelAdmin):
    list_display = ("id", "recipe", "ingredient", "quantity")
    list_filter = ("ingredient",)
    search_fields = ("ingredient__name",)

@admin.register(InventoryMovement)
class InventoryMovementAdmin(admin.ModelAdmin):
    list_display = ("id", "ingredient", "quantity", "movement_type", "timestamp")
    list_filter = ("movement_type", "timestamp")
    date_hierarchy = "timestamp"
    search_fields = ("ingredient__name",)
