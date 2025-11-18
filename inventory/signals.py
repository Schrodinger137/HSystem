from django.db.models.signals import post_save
from django.dispatch import receiver
from sales.models import SaleItem
from inventory.models import RecipeIngredient, InventoryMovement

@receiver(post_save, sender=SaleItem)
def descontar_inventario(sender, instance, created, **kwargs):
    if not created:
        return

    product = instance.product
    cantidad_vendida = instance.quantity

    ingredientes = RecipeIngredient.objects.filter(recipe__product=product)

    for ri in ingredientes:
        cantidad_usada = ri.quantity * cantidad_vendida

        InventoryMovement.objects.create(
            ingredient=ri.ingredient,
            quantity=-cantidad_usada,
            movement_type="salida"
        )
