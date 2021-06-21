from django.urls import path
from Carrito.views import agregar_producto, eliminar_producto, limpiar_carrito, restar_producto

app_name = "carrito"

urlpatterns = [
    path('agregar/<int:producto_id>/', agregar_producto, name="agregar"),
    path('restar/<int:producto_id>/', restar_producto, name="restar"),
    path('eliminar/<int:producto_id>/', eliminar_producto, name="eliminar"),
    path('limpiar/', limpiar_carrito, name="limpiar"),
]
