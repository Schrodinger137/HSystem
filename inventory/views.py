from decimal import Decimal
from django.shortcuts import render
from .models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404


# Create your views here.
def index(request):
    return render(request, 'principal/index.html')

def inventory(request):
    
    ingredients = Ingredient.objects.all()    
    recent_ingredients = Ingredient.objects.order_by('-created_at')[:5]
    total_ingredients = ingredients.count()
    total_cost_ingredients = sum([ingredient.total_cost for ingredient in ingredients])
    
    context = {
        'ingredients':ingredients,
        'recent_ingredients':recent_ingredients,
        'total_cost_ingredients':total_cost_ingredients,
        'total_ingredients':total_ingredients,
    }

    return render(request, 'inventory/inventory.html', context)

def ingredientInventory(request):
    ingredients = Ingredient.objects.all()

    context = {
        'ingredients': ingredients,
    }

    return render(request, 'inventory/ingredientInventory.html', context)

@require_POST
def ingredient_create(request):
    try:
        name = request.POST.get("name")
        unit = request.POST.get("unit")
        cost_per_unit = Decimal(request.POST.get("cost_per_unit"))
        quantity = Decimal(request.POST.get("quantity", "0"))

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
            }
        })

    except Exception as e:
        return JsonResponse({
            "success": False,
            "message": str(e)
        }, status=500)
        
@require_POST
def ingredient_update(request, ingredient_id):
    try:
        ingredient = get_object_or_404(Ingredient, id=ingredient_id)

        name = request.POST.get("name")
        unit = request.POST.get("unit")
        cost_per_unit = Decimal(request.POST.get("cost_per_unit"))
        quantity = Decimal(request.POST.get("quantity", "0"))

        if not name or not unit:
            return JsonResponse({
                "success": False,
                "message": "Todos los campos son obligatorios"
            }, status=400)

        ingredient.name = name
        ingredient.unit = unit
        ingredient.cost_per_unit = cost_per_unit
        ingredient.quantity = quantity
        ingredient.save()

        return JsonResponse({
            "success": True,
            "message": "Ingrediente actualizado correctamente",
            "ingredient": {
                "id": ingredient.id,
                "name": ingredient.name,
                "unit": ingredient.unit,
                "cost_per_unit": str(ingredient.cost_per_unit),
                "quantity": str(ingredient.quantity),
                "total_cost": str(ingredient.total_cost),
            }
        })

    except Exception as e:
        return JsonResponse({
            "success": False,
            "message": str(e)
        }, status=500)        

def ingredientsStatistics(request):
    return render(request, 'inventory/statistics/ingredientStatistic.html')

def ingredient(request, ingredient_id):
    
    ingredient = get_object_or_404(Ingredient, id=ingredient_id)
    
    context={
        'ingredient':ingredient
    }
    
    return render(request, 'inventory/ingredient.html', context)

def recipeInventory(request):
    return render(request, 'inventory/recipeInventory.html')