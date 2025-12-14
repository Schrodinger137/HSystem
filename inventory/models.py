from django.db import models
from products.models import *
from django.db.models import Sum
from decimal import Decimal

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    unit = models.CharField(max_length=20)
    cost_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)  # <- sin default
    updated_at = models.DateTimeField(auto_now=True)

    
    def save(self, *args, **kwargs):
        # Regla de negocio central
        self.available = self.quantity > Decimal("0")
        super().save(*args, **kwargs)

    
    @property
    def total_cost(self):
        return self.cost_per_unit * self.quantity
    
    def entradas(self):
        return (
            self.inventorymovement_set
                .filter(movement_type="entrada")
                .aggregate(total=Sum("quantity"))["total"]
            or 0
        )

    def salidas(self):
        return (
            self.inventorymovement_set
                .filter(movement_type="salida")
                .aggregate(total=Sum("quantity"))["total"]
            or 0
        )

    def stock_actual(self):
        return self.entradas() + self.salidas()

    def __str__(self):
        return self.name

class Recipe(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    ingredients = models.ManyToManyField(
        Ingredient,
        through="RecipeIngredient",
        related_name="recipes"
    )

    def __str__(self):
        return f"Receta de {self.product}"

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.ingredient} en {self.recipe}: {self.quantity}"

class InventoryMovement(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    movement_type = models.CharField(max_length=20)  # entrada / salida / merma
    timestamp = models.DateTimeField(auto_now_add=True)