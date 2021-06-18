from django.shortcuts import render
from .models import ProdTienda


def tienda(request):

    productos = ProdTienda.objects.all()

    return render(request, "Tienda/tienda.html", {"productos": productos})
