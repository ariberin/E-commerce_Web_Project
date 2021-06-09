from django.contrib import admin

from .models import Producto


class ProductoAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")

admin.site.register(Producto, ProductoAdmin)
