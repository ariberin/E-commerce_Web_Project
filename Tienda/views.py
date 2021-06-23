from django.shortcuts import render
from Tienda.models import Producto, Categoria


def tienda(request):

    productos = Producto.objects.all()

    return render(request, "Tienda/tienda.html", {"productos": productos})

def categoria(request, categoria_id):

    categorias = Categoria.objects.get(id=categoria_id)

    productos = Producto.objects.filter(categorias=categorias)

    return render(request, "Tienda/categorias2.html", {"categorias": categorias, "productos": productos})