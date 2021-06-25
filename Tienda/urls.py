from django.urls import path
from Tienda.views import tienda, categoria

urlpatterns = [
    path('', tienda, name="Tienda"),
    path('categoria/<categoria_id>/', categoria, name="Categorias2"),
]
