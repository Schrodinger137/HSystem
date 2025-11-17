from django.contrib import admin
from .models import * 

# Register your models here.

admin.site.register(Ingredient)
admin.site.register(RecipeIngredient)

class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 1

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInline]
