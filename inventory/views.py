from django.shortcuts import render
from .models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST


# Create your views here.
def index(request):
    return render(request, 'principal/index.html')

def inventory(request):
    
    ingredients = Ingredient.objects.all()
    
    context = {
        'ingredients':ingredients
    }

    return render(request, 'inventory/inventory.html', context)

def ingredientInventory(request):
    ingredients = Ingredient.objects.all()

    context = {
        'ingredients': ingredients
    }

    return render(request, 'inventory/ingredientInventory.html', context)

@require_POST
def ingredient_create(request):
    try:
        name = request.POST.get("name")
        unit = request.POST.get("unit")
        cost_per_unit = Decimal(request.POST.get("cost_per_unit"))
        quantity = Decimal(request.POST.get("quantity", "0"))
        available = request.POST.get("available") == "on"

        if not name or not unit:
            return JsonResponse({
                "success": False,
                "message": "Todos los campos son obligatorios"
            }, status=400)

        ingredient = Ingredient.objects.create(
            name=name,
            unit=unit,
            cost_per_unit=cost_per_unit,
            quantity=quantity,
            available=available
        )

        return JsonResponse({
            "success": True,
            "message": "Ingrediente creado correctamente",
            "ingredient": {
                "id": ingredient.id,
                "name": ingredient.name,
                "unit": ingredient.unit,
                "cost_per_unit": str(ingredient.cost_per_unit),
                "quantity": str(ingredient.quantity),
                "total_cost": str(ingredient.total_cost),
                "available": ingredient.available
            }
        })

    except Exception as e:
        return JsonResponse({
            "success": False,
            "message": str(e)
        }, status=500)

def recipeInventory(request):
    return render(request, 'inventory/recipeInventory.html')