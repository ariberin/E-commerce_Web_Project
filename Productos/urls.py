from django.contrib import admin
from django.urls import path
from .views import productos

urlpatterns = [
    path('', productos, name="Productos"),

]
