from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'principal/index.html')

def inventory(request):
    return render(request, 'inventory/inventory.html')

def ingredientInventory(request):
    return render(request, 'inventory/ingredientInventory.html')

def recipeInventory(request):
    return render(request, 'inventory/recipeInventory.html')