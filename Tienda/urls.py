from django.urls import path
from Tienda.views import tienda

urlpatterns = [
    path('', tienda, name="Tienda"),
]
