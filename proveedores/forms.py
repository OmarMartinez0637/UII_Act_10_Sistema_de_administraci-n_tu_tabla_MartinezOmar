from django import forms
from .models import Proveedor

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['id_proveedor', 'nombre', 'telefono', 'email', 'direccion', 'producto_suministrado']
        # Podemos añadir atributos de Bootstrap a los widgets para un mejor estilo
        widgets = {
            'id_proveedor': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'producto_suministrado': forms.TextInput(attrs={'class': 'form-control'}),
        }