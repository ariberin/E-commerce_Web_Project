from django.db.models.deletion import CASCADE
from django.db.models.fields import *
from django.db import models
from django.db.models.fields.files import ImageField
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey, ManyToManyField

class Categoria(models.Model):  # Mapeo ORM
    nombre = CharField(max_length=30)
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self):
        return self.nombre

class Post(models.Model):
    titulo = CharField(max_length=100)
    contenido = CharField(max_length=500)
    imagen = ImageField(upload_to='blog') #opcional
    autor = ForeignKey(User, on_delete=CASCADE)
    #relacion uno a muchos en la bbdd, un ator a muchos post, cuando se elimna un autor, se eliminan sus post
    categorias = ManyToManyField(Categoria)
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'

    def __str__(self):
        return self.titulo

    
