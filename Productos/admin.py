from django.contrib import admin

from Productos.models import Producto


class ProductoAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")

admin.site.register(Producto, ProductoAdmin)
