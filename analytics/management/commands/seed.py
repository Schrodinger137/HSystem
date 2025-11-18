from django.core.management.base import BaseCommand
from products.models import Product
from inventory.models import Ingredient, Recipe, RecipeIngredient, InventoryMovement
from sales.models import Sale, SaleItem


class Command(BaseCommand):
    help = "Llena la base de datos con datos de prueba"

    def handle(self, *args, **kwargs):

        # === Ingredientes ===
        pan = Ingredient.objects.create(name="Pan", unit="pieza", cost_per_unit=3)
        carne = Ingredient.objects.create(name="Carne", unit="gr", cost_per_unit=0.30)
        queso = Ingredient.objects.create(name="Queso", unit="gr", cost_per_unit=0.25)
        lechuga = Ingredient.objects.create(name="Lechuga", unit="gr", cost_per_unit=0.10)
        papa = Ingredient.objects.create(name="Papa", unit="gr", cost_per_unit=0.05)

        self.stdout.write(self.style.SUCCESS("Ingredientes creados"))

        # === Productos ===
        hamb = Product.objects.create(
            name="Hamburguesa Clásica",
            description="Pan, carne, queso y vegetales",
            precio=95,
            available=True,
        )

        papas = Product.objects.create(
            name="Papas Fritas",
            description="Papas fritas crujientes",
            precio=40,
            available=True,
        )

        self.stdout.write(self.style.SUCCESS("Productos creados"))

        # === Receta hamburguesa ===
        receta_hamb = Recipe.objects.create(product=hamb)

        RecipeIngredient.objects.create(recipe=receta_hamb, ingredient=pan, quantity=1)
        RecipeIngredient.objects.create(recipe=receta_hamb, ingredient=carne, quantity=120)
        RecipeIngredient.objects.create(recipe=receta_hamb, ingredient=queso, quantity=30)
        RecipeIngredient.objects.create(recipe=receta_hamb, ingredient=lechuga, quantity=15)

        self.stdout.write(self.style.SUCCESS("Receta creada"))

        # === Inventario inicial ===
        InventoryMovement.objects.create(ingredient=pan, quantity=30, movement_type="entrada")
        InventoryMovement.objects.create(ingredient=carne, quantity=5000, movement_type="entrada")
        InventoryMovement.objects.create(ingredient=queso, quantity=2000, movement_type="entrada")
        InventoryMovement.objects.create(ingredient=lechuga, quantity=1500, movement_type="entrada")
        InventoryMovement.objects.create(ingredient=papa, quantity=3000, movement_type="entrada")

        self.stdout.write(self.style.SUCCESS("Inventario cargado"))

        # === Venta de prueba ===
        venta = Sale.objects.create(order_type="local")

        # Hamburguesa × 2 (sí tiene receta → descontará inventario)
        SaleItem.objects.create(
            sale=venta,
            product=hamb,
            quantity=2,
            price=hamb.precio,
        )

        # Papas × 1 (NO tiene receta; no descontará nada)
        SaleItem.objects.create(
            sale=venta,
            product=papas,
            quantity=1,
            price=papas.precio,
        )

        self.stdout.write(self.style.SUCCESS("Venta creada con productos y recetas válidas"))

        self.stdout.write(self.style.SUCCESS("Seed completado con ventas incluidas"))
