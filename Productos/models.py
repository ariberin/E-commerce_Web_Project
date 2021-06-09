from django.db.models.fields import *
from django.db import models
from django.db.models.fields.files import ImageField


class Producto(models.Model): #Mapeo ORM
    titulo = CharField(max_length=30)
    contenido = CharField(max_length=50)
    imagen = ImageField(upload_to = 'productos')
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'productos'

    def __str__(self):
        return self.titulo