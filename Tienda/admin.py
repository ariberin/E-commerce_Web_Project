from django.contrib import admin

from .models import CategoriaProducto, ProductoTienda


class CateProdAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")

class ProdTienAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")


admin.site.register(CategoriaProducto, CateProdAdmin)
admin.site.register(ProductoTienda, ProdTienAdmin)
