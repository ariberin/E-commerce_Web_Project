from django.db.models.deletion import CASCADE
from django.db.models.fields import *
from django.db import models
from django.db.models.fields.files import ImageField
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey, ManyToManyField


class CategoriaProducto(models.Model):  # Mapeo ORM
    nombre = CharField(max_length=200)
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'categoriaProducto'
        verbose_name_plural = 'categoriasProductos'

    def __str__(self):
        return self.nombre


class ProductoTienda(models.Model):
    nombre = CharField(max_length=100)
    categorias = ForeignKey(CategoriaProducto, on_delete=CASCADE)
    imagen = ImageField(upload_to='tienda')
    precio = FloatField()
    disponibilidad = BooleanField(default=True)
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'productos'

    def __str__(self):
        return self.titulo
