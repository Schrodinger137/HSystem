"""
URL configuration for HSystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from inventory import views as inv_views
from products import views as prod_views
from sales import views as sales_views
from finance import views as fin_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inv_views.index, name='index'),
    path('inventory', inv_views.inventory, name='inventory'),
    path('ingredientInventory', inv_views.ingredientInventory, name='ingredientInventory'),
    path("ingredients/create/", inv_views.ingredient_create, name="ingredientCreate"),
    path("ingredients/<int:ingredient_id>/update/", inv_views.ingredient_update, name="ingredientUpdate"),
    path('recipeInventory', inv_views.recipeInventory, name='recipeInventory'),
    path('products/', prod_views.products, name='products'),
    path('sales/', sales_views.sales, name='sales'),
    path('finance/', fin_views.finance, name='finance'),
]
