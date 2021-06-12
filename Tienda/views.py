from django.shortcuts import render
from .models import ProductoTienda


def tienda(request):

    productos = ProductoTienda.objects.all()

    return render(request, "Tienda/tienda.html", {"productos": productos})
