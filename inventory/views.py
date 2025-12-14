from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    return render(request, 'principal/index.html')

def inventory(request):
    return render(request, 'inventory/inventory.html')

def ingredientInventory(request):
    ingredients = Ingredient.objects.all()

    context = {
        'ingredients': ingredients
    }

    return render(request, 'inventory/ingredientInventory.html', context)

def recipeInventory(request):
    return render(request, 'inventory/recipeInventory.html')