from django.shortcuts import render
from .models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

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

@csrf_exempt  # luego te explico cómo quitarlo correctamente
def ingredient_create(request):
    if request.method == "POST":
        name = request.POST.get("name")
        unit = request.POST.get("unit")
        cost_per_unit = request.POST.get("cost_per_unit")
        available = request.POST.get("available") == "on"

        # Validaciones básicas
        if not name or not unit or not cost_per_unit:
            return JsonResponse({
                "success": False,
                "message": "Todos los campos son obligatorios"
            }, status=400)

        ingredient = Ingredient.objects.create(
            name=name,
            unit=unit,
            cost_per_unit=cost_per_unit,
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
                "available": ingredient.available
            }
        })

    return JsonResponse({
        "success": False,
        "message": "Método no permitido"
    }, status=405)


def recipeInventory(request):
    return render(request, 'inventory/recipeInventory.html')