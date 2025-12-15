from django.shortcuts import render
from .models import *
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from decimal import Decimal

# Create your views here.
def products(request):
    products = Product.objects.all()
    
    context = {
        'products':products
    }

    return render(request, 'products/products.html', context)

@require_POST
def product_create(request):
    try: 
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        available = request.POST.get('available') == 'on'  # Checkbox devuelve 'on' si está marcado

        # Validación básica
        if not name or not description or not price:
            return JsonResponse({'success': False, 'message': 'Todos los campos son obligatorios.'})

        # Convertir precio a entero
        try:
            price = int(price)
        except ValueError:
            return JsonResponse({'success': False, 'message': 'El precio debe ser un número válido.'})

        # Crear el producto
        product = Product.objects.create(
            name=name,
            description=description,
            price=price,
            available=available
        )

        return JsonResponse({'success': True, 'message': 'Producto creado correctamente.'})

    except Exception as e:
        return JsonResponse({'success': False, 'message': f'Ocurrió un error: {str(e)}'})
