from django.contrib import admin
from .models import Proveedor

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('id_proveedor', 'nombre', 'producto_suministrado', 'email', 'telefono', 'direccion')
    search_fields = ('nombre', 'producto_suministrado', 'id_proveedor', 'email')
    list_filter = ('producto_suministrado',)
    # list_per_page = 20 # Opcional: número de elementos por página en el admin