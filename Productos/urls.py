from django.contrib import admin
from django.urls import path
from Productos.views import productos

urlpatterns = [
    path('', productos, name="Productos"),

]
