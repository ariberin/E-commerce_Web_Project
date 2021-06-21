from django.shortcuts import redirect
from .carrito import Carrito
from Tienda.models import Producto


def agregar_producto(request, producto_id):

    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    
    carrito.agregar(producto=producto)

    return redirect("Tienda")

def eliminar_producto(request, producto_id):

    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    
    carrito.eliminar(producto=producto)

    return redirect("Tienda")

def restar_producto(request, producto_id):

    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)

    carrito.restar(producto=producto)

    return redirect("Tienda")

def limpiar_carrito(request):

    carrito = Carrito(request)
    carrito.limpiar()

    return redirect("Tienda")
