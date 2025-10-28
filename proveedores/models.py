from django.db import models

class Proveedor(models.Model):
    id_proveedor = models.CharField(max_length=20, unique=True, verbose_name="ID del Proveedor")
    nombre = models.CharField(max_length=100, verbose_name="Nombre del Proveedor")
    telefono = models.CharField(max_length=15, blank=True, null=True, verbose_name="Teléfono")
    email = models.EmailField(unique=True, verbose_name="Correo Electrónico")
    direccion = models.CharField(max_length=255, verbose_name="Dirección")
    producto_suministrado = models.CharField(max_length=100, verbose_name="Producto Suministrado")

    def __str__(self):
        return f"{self.nombre} ({self.producto_suministrado})"

    class Meta:
        ordering = ['nombre'] # Ordenar proveedores por nombre por defecto
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"