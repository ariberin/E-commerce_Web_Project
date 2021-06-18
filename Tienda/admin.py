from django.contrib import admin
from .models import CategoriaProd, ProdTienda


class CategoriaProductoAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")


class ProductoTiendaAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")


admin.site.register(CategoriaProd, CategoriaProductoAdmin)
admin.site.register(ProdTienda, ProductoTiendaAdmin)
