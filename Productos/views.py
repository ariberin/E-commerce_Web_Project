from django.shortcuts import render
from Productos.models import Producto

def productos(request):

    productos = Producto.objects.all()

    return render(request, "Productos/productos.html", {"productos": productos})
