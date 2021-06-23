from django.shortcuts import redirect, render
from .carrito import Carrito
from Tienda.models import Producto

def carrito_carrito(request):
    
    carrito1 = Carrito(request)

    return render(request, "Carrito/widget.html", {"carrito":carrito1})

def agregar_producto(request, producto_id):

    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    
    carrito.agregar(producto=producto)

    return redirect("/widget/")

def eliminar_producto(request, producto_id):

    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    
    carrito.eliminar(producto=producto)

    return redirect("/widget/")

def restar_producto(request, producto_id):

    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)

    carrito.restar(producto=producto)

    return redirect("/widget/")

def limpiar_carrito(request):

    carrito = Carrito(request)
    carrito.limpiar()

    return redirect("/widget/")
