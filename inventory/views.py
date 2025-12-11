from django.shortcuts import render

# Create your views here.
def index(request):
    labels = ["Ene", "Feb", "Mar", "Abr", "May"]
    ventas = [150, 200, 180, 220, 300]
    gastos = [120, 160, 130, 150, 210]

    context = {
        "labels": labels,
        "ventas": ventas,
        "gastos": gastos,
    }
    return render(request, 'principal/index.html', context)